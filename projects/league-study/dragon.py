"""Look up champion data from Riot's public Data Dragon endpoint."""
import argparse
import json
import re
from urllib.error import URLError
from urllib.request import urlopen

BASE_URL = 'https://ddragon.leagueoflegends.com'


def get_json(path):
    with urlopen(BASE_URL + path, timeout=20) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description='Consulta pública de campeões no Data Dragon')
    parser.add_argument('champion', help='ID do campeão, por exemplo Ahri ou MonkeyKing')
    parser.add_argument('--patch', help='Versão do Data Dragon, por exemplo 16.23.1')
    args = parser.parse_args()
    if args.patch and not re.fullmatch(r'\d+\.\d+\.\d+', args.patch):
        parser.error('Informe o patch no formato X.Y.Z.')

    try:
        patch = args.patch or get_json('/api/versions.json')[0]
        data = get_json(f'/cdn/{patch}/data/pt_BR/champion.json')['data']
    except (URLError, TimeoutError, ValueError, KeyError, IndexError) as error:
        parser.exit(1, f'Falha ao consultar o Data Dragon: {error}\n')

    candidates = {champion_id.casefold(): item for champion_id, item in data.items()}
    champion = candidates.get(args.champion.casefold())
    if champion is None:
        parser.exit(1, f'{args.champion} não encontrado no patch {patch}. Use o ID do Data Dragon.\n')

    print(json.dumps({
        'patch': patch,
        'id': champion['id'],
        'nome': champion['name'],
        'titulo': champion['title'],
        'atributos': champion['stats'],
    }, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
