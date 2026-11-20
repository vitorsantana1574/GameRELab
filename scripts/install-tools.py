"""Install the pinned Windows ZIP tools inside this checkout."""
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import tempfile
from urllib.request import Request, urlopen
import zipfile

ROOT = Path(__file__).resolve().parents[1]
TOOLS_DIR = ROOT / "tools"


def download(url, output):
    request = Request(url, headers={"User-Agent": "GameRELab/1.0"})
    with urlopen(request, timeout=45) as response, output.open("wb") as stream:
        shutil.copyfileobj(response, stream, length=1024 * 1024)


def published_checksum(tool, work, filename):
    if "sha256" in tool:
        return tool["sha256"]
    if "checksums" not in tool:
        return None
    listing = work / "SHA256SUMS"
    download(tool["checksums"], listing)
    for line in listing.read_text(encoding="utf-8").splitlines():
        fields = line.split()
        if len(fields) == 2 and fields[1].lstrip("*") == filename:
            return fields[0].lower()
    raise ValueError(f"Checksum oficial ausente para {filename}")


def extract(archive, output):
    with zipfile.ZipFile(archive) as source:
        for member in source.infolist():
            parts = PurePosixPath(member.filename.replace("\\", "/")).parts
            if any(part in {"..", "/"} or ":" in part for part in parts):
                raise ValueError(f"Caminho inesperado no ZIP: {member.filename}")
        source.extractall(output)


def install(tool):
    tool_id = tool["id"]
    target = TOOLS_DIR / tool_id / tool["version"]
    if target.is_dir():
        return f"{tool_id}: {tool['version']} já presente"
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".install-", dir=target.parent) as folder:
        work = Path(folder)
        archive = work / tool["url"].rsplit("/", 1)[1]
        download(tool["url"], archive)
        if "bytes" in tool and archive.stat().st_size != tool["bytes"]:
            raise ValueError(f"Tamanho inesperado para {archive.name}")
        expected = published_checksum(tool, work, archive.name)
        with archive.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        if expected is not None and digest != expected:
            raise ValueError(f"SHA-256 incorreto para {archive.name}")
        extracted = work / "extracted"
        extract(archive, extracted)
        extracted.rename(target)
    return f"{tool_id}: {tool['version']} instalado (SHA-256 {digest})"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tools", nargs="*", help="IDs em manifests/tools.windows.json")
    parser.add_argument("--jobs", type=int, default=4)
    args = parser.parse_args()
    manifest = json.loads((ROOT / "manifests/tools.windows.json").read_text(encoding="utf-8"))
    by_id = {tool["id"]: tool for tool in manifest}
    unknown = set(args.tools) - by_id.keys()
    if unknown:
        parser.error(f"Ferramentas desconhecidas: {', '.join(sorted(unknown))}")
    if not 1 <= args.jobs <= 8:
        parser.error("--jobs deve ficar entre 1 e 8")
    selected = args.tools or list(by_id)
    failures = 0
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        plans = {tool_id: pool.submit(install, by_id[tool_id]) for tool_id in dict.fromkeys(selected)}
        for tool_id, future in plans.items():
            try:
                print(future.result(), flush=True)
            except Exception as exc:
                failures += 1
                print(f"{tool_id}: falhou ({exc})", flush=True)
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
