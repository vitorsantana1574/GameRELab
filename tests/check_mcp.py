"""Verify discovery, allowed reads, and rejection of local-only paths."""
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
server = root / 'scripts/lab-mcp.py'
requests = [
    ('initialize', {'protocolVersion': '2025-11-25'}),
    ('tools/list', {}),
    ('tools/call', {'name': 'list_lab_files'}),
    ('tools/call', {'name': 'read_lab_file', 'arguments': {'path': 'docs/MINECRAFT.md'}}),
    ('tools/call', {'name': 'read_lab_file', 'arguments': {'path': 'sandbox/README.md'}}),
]
payload = '\n'.join(json.dumps({'jsonrpc': '2.0', 'id': index, 'method': method, 'params': params})
                    for index, (method, params) in enumerate(requests, start=1))
process = subprocess.run([sys.executable, str(server)], text=True, input=payload + '\n',
                         capture_output=True, check=True, timeout=10)
results = [json.loads(line)['result'] for line in process.stdout.splitlines()]
assert results[0]['serverInfo']['name'] == 'gamerelab'
assert {tool['name'] for tool in results[1]['tools']} == {'list_lab_files', 'read_lab_file'}
assert 'docs/MINECRAFT.md' in results[2]['content'][0]['text']
assert 'Cobblemon' in results[3]['content'][0]['text']
assert results[4]['isError']
print('GameRELab MCP: 5 verificações passaram.')
