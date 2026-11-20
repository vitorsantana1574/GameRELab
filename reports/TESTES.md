# Testes da implantação

| Verificação | Resultado observado |
| --- | --- |
| JDK 21 e 25 | Executaram `javac -version`. |
| Node 24 | Executou `node --version`. |
| Blender | Iniciou em modo sem interface, executou um comando Python e retornou os objetos da cena inicial. |
| me3 | Executou `--version`. |
| Ghidra | Importou e analisou `DamagePreview.class`, compilado do código do laboratório, com o analisador sem interface. |
| ILSpy | O descompilador da instalação portátil recuperou o método `Main` e sua mensagem em uma DLL .NET 10 de teste. |
| REA | A inspeção estática recuperou a identidade de `GameRELabSample.dll`. |
| Craft Anything | A versão portátil executou `craft-anything-cli --version` e retornou 0.6.1. |
| Data Dragon | A consulta real de Ahri retornou dados em português brasileiro. |
| MCP do laboratório | Cinco verificações locais passaram, incluindo listar e ler o guia Minecraft. |
| Codex | Registro stdio confirmado no perfil isolado. |
| Claude Code | O teste stdio do cliente exibiu `Connected` após o registro explícito no perfil isolado. A entrada automática de `.mcp.json` pede autorização no perfil normal. |
| Fabric local | Gradle e Fabric Loom iniciaram. O acesso Java ao caminho canônico do JAR do Minecraft falhou no cache da sessão de Windows. |
| GitHub Actions | A [primeira execução](https://github.com/vitorsantana1574/GameRELab/actions/runs/44827982666) passou na compilação Fabric no Linux e no teste do protocolo MCP no Windows. |
| Baldur’s Gate 3 | A instalação base foi encontrada. O Toolkit e seu DLC de dados ainda aguardam instalação pela Steam. |
| Testes dentro dos jogos | Comando `/gamerelab` em um mundo, conexão com outro cliente pelo Radmin e fluxo de modding de Elden Ring ainda precisam de validação. |
