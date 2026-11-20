[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$smithbox = Get-ChildItem -Path (Join-Path $root 'tools/smithbox') -Filter Smithbox.Vulkan.exe `
    -Recurse -File -ErrorAction SilentlyContinue | Select-Object -First 1
if (!$smithbox) { throw 'Execute python scripts/install-tools.py smithbox.' }

$localData = [Environment]::GetFolderPath([Environment+SpecialFolder]::LocalApplicationData)
if (!$localData) { throw 'O Windows não informou a pasta LocalAppData do usuário.' }

$config = Join-Path $localData 'Smithbox/Configuration'
try {
    [System.IO.Directory]::CreateDirectory($config) | Out-Null
    $probe = Join-Path $config ('gamerelab-' + [Guid]::NewGuid().ToString('N') + '.tmp')
    $stream = [System.IO.FileStream]::new($probe, [System.IO.FileMode]::CreateNew,
        [System.IO.FileAccess]::Write, [System.IO.FileShare]::None, 1,
        [System.IO.FileOptions]::DeleteOnClose)
    $stream.Dispose()
} catch [System.UnauthorizedAccessException] {
    throw "O Windows negou acesso à pasta de preferências do Smithbox: $config"
}

Start-Process -FilePath $smithbox.FullName -WorkingDirectory $smithbox.DirectoryName
