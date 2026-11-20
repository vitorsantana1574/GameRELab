[CmdletBinding()]
param(
    [ValidateSet('build', 'runClient', 'runServer')]
    [string]$Task = 'build'
)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$java = Get-ChildItem -Path (Join-Path $root 'tools/jdk21') -Filter javac.exe -Recurse -File -ErrorAction SilentlyContinue |
    Select-Object -First 1
$gradle = Get-ChildItem -Path (Join-Path $root 'tools/gradle') -Filter gradle.bat -Recurse -File -ErrorAction SilentlyContinue |
    Select-Object -First 1
if (!$java -or !$gradle) { throw 'Execute python scripts/install-tools.py jdk21 gradle.' }

$env:JAVA_HOME = Split-Path -Parent $java.DirectoryName
$env:GRADLE_USER_HOME = Join-Path $root 'sandbox/gradle'
& $gradle.FullName --no-daemon --console=plain -p (Join-Path $root 'projects/minecraft') $Task
exit $LASTEXITCODE
