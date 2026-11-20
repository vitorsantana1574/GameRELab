# Ferramentas para Windows

O instalador `python scripts/install-tools.py <id> [...]` baixa os ZIPs do [manifesto](../manifests/tools.windows.json) e extrai cada versão em `tools/<id>/<versão>/`. Ele verifica SHA-256 quando há um valor no manifesto ou no arquivo de checksums do fornecedor. Para os demais pacotes, a verificação se limita às informações disponíveis no manifesto e à leitura do ZIP.

| IDs | Uso no laboratório |
| --- | --- |
| `jdk21`, `gradle` | Compilação e ambiente de desenvolvimento Fabric. |
| `jdk25`, `ghidra` | Análise estática da amostra de software. [Documentação do Ghidra](https://github.com/NationalSecurityAgency/ghidra/blob/master/GhidraDocs/GettingStarted.md) |
| `imhex`, `ilspy`, `x64dbg`, `procmon` | Inspeção hexadecimal, código .NET, depuração de software próprio e monitoramento de arquivos de um programa. |
| `blender`, `renderdoc`, `tracy` | Criação de modelos e diagnóstico gráfico ou de desempenho de projetos próprios. |
| `assetripper`, `bepinex`, `ue4ss` | Ferramentas específicas para projetos Unity e Unreal compatíveis. |
| `smithbox`, `me3`, `dsanimstudio`, `hkbeditor`, `witchybnd`, `darkscript3` | Ferramentas de dados, animações e eventos para Elden Ring. |
| `github-cli`, `node24` | GitHub CLI e runtime Node.js portátil. |

O [relatório de testes](../reports/TESTES.md) diferencia arquivos presentes de ferramentas executadas. A versão exata de cada pacote fica no manifesto.
