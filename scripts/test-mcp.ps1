[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$env:CODEX_HOME = Join-Path $root 'sandbox/codex-mcp'
New-Item -ItemType Directory -Path $env:CODEX_HOME -Force | Out-Null
$serverPath = Join-Path $root 'scripts/lab-mcp.py'
$pythonPath = (Get-Command python -CommandType Application | Select-Object -First 1).Source

Push-Location $root
try {
    & $pythonPath (Join-Path $root 'tests/check_mcp.py')
    if ($LASTEXITCODE) { exit $LASTEXITCODE }

    claude mcp list
    if ($LASTEXITCODE) { exit $LASTEXITCODE }

    codex mcp add gamerelab -- $pythonPath $serverPath
    if ($LASTEXITCODE) { exit $LASTEXITCODE }
    codex mcp get gamerelab
    if ($LASTEXITCODE) { exit $LASTEXITCODE }
} finally {
    Pop-Location
}
