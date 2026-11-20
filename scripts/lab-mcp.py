"""Read-only MCP server exposing GameRELab guides and example source."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TOOLS = [
    {
        'name': 'list_lab_files',
        'description': 'Lista guias e código-fonte dos exemplos do GameRELab.',
        'inputSchema': {'type': 'object', 'properties': {}, 'additionalProperties': False},
    },
    {
        'name': 'read_lab_file',
        'description': 'Lê um guia ou fonte retornado por list_lab_files.',
        'inputSchema': {
            'type': 'object',
            'properties': {'path': {'type': 'string'}},
            'required': ['path'],
            'additionalProperties': False,
        },
    },
]


def published_files():
    paths = [ROOT / 'README.md', *ROOT.glob('docs/*.md'), *ROOT.glob('reports/*.md')]
    paths += list(ROOT.glob('projects/*/README.md'))
    paths += list(ROOT.glob('projects/minecraft/src/main/java/**/*.java'))
    paths += [ROOT / 'projects/software-analysis/DamagePreview.java',
              ROOT / 'projects/league-study/dragon.py']
    return {path.relative_to(ROOT).as_posix(): path for path in paths
            if path.is_file() and path.resolve().is_relative_to(ROOT)}


def call_tool(params):
    files = published_files()
    name = params.get('name')
    if name == 'list_lab_files':
        return {'content': [{'type': 'text', 'text': '\n'.join(sorted(files))}]}
    if name == 'read_lab_file':
        arguments = params.get('arguments') or {}
        path = files.get(arguments.get('path'))
        if path is not None:
            return {'content': [{'type': 'text', 'text': path.read_text(encoding='utf-8')}]}
    return {'isError': True, 'content': [{'type': 'text', 'text': 'Arquivo ou ferramenta indisponível.'}]}


def reply(request):
    if 'id' not in request:
        return None
    message = {'jsonrpc': '2.0', 'id': request['id']}
    params = request.get('params') or {}
    match request.get('method'):
        case 'initialize':
            requested = params.get('protocolVersion')
            supported = ('2024-11-05', '2025-03-26', '2025-06-18', '2025-11-25')
            message['result'] = {
                'protocolVersion': requested if requested in supported else supported[-1],
                'capabilities': {'tools': {}},
                'serverInfo': {'name': 'gamerelab', 'version': '1.0.0'},
            }
        case 'ping':
            message['result'] = {}
        case 'tools/list':
            message['result'] = {'tools': TOOLS}
        case 'tools/call':
            message['result'] = call_tool(params)
        case _:
            message['error'] = {'code': -32601, 'message': 'Method not found'}
    return message


if __name__ == '__main__':
    for line in sys.stdin:
        try:
            output = reply(json.loads(line))
        except (ValueError, TypeError, AttributeError, OSError):
            output = {'jsonrpc': '2.0', 'id': None,
                      'error': {'code': -32600, 'message': 'Invalid request'}}
        if output is not None:
            print(json.dumps(output), flush=True)
