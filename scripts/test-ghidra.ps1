[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$javac = Get-ChildItem -Path (Join-Path $root 'tools/jdk25') -Filter javac.exe -Recurse -File |
    Select-Object -First 1
$ghidra = Get-ChildItem -Path (Join-Path $root 'tools/ghidra') -Filter analyzeHeadless.bat -Recurse -File |
    Select-Object -First 1
if (!$javac -or !$ghidra) { throw 'Execute python scripts/install-tools.py jdk25 ghidra.' }

$work = Join-Path $root 'sandbox/ghidra-sample'
New-Item -ItemType Directory -Path $work -Force | Out-Null
$env:JAVA_HOME = $javac.Directory.Parent.FullName
$env:PATH = "$($javac.DirectoryName);$env:PATH"
$env:XDG_CONFIG_HOME = Join-Path $work 'config'
$env:XDG_CACHE_HOME = Join-Path $work 'cache'
& $javac.FullName -source 17 -target 17 -Xlint:-options -d $work (Join-Path $root 'projects/software-analysis/DamagePreview.java')
if ($LASTEXITCODE) { exit $LASTEXITCODE }

$fixture = 'fixture-' + [Guid]::NewGuid().ToString('N')
& $ghidra.FullName $work $fixture -import (Join-Path $work 'DamagePreview.class') -deleteProject
exit $LASTEXITCODE
