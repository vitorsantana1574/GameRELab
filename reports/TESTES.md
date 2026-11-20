# Testes da implantação

| Verificação | Resultado observado |
| --- | --- |
| JDK 21 e 25 | Executaram `javac -version`. |
| Node 24 | Executou `node --version`. |
| Blender | Iniciou em modo sem interface, executou um comando Python e retornou os objetos da cena inicial. |
| me3 | Executou `--version`. |
| Data Dragon | A consulta real de Ahri retornou dados em português brasileiro. |
| MCP do laboratório | Cinco verificações locais passaram, incluindo listar e ler o guia Minecraft. |
| Codex | Registro stdio confirmado no perfil isolado. |
| Claude Code | Detectou o servidor do projeto e indicou autorização pendente. |
| Fabric local | Gradle e Fabric Loom iniciaram. O acesso Java ao caminho canônico do JAR do Minecraft falhou no cache do Windows. A compilação também está configurada no GitHub Actions. |
| Games | Teste de carregamento do mod dentro do jogo, fluxo offline completo de Elden Ring e criação de um mod BG3 ainda precisam de validação. |
