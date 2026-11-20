# Claude Code

Abra o Claude Code na raiz do repositório. O `CLAUDE.md` referencia as instruções comuns do projeto. Para localizar inicializadores e comandos Java, use `rg -n 'onInitialize|CommandRegistrationCallback' projects/minecraft`.

O repositório inclui `scripts/lab-mcp.py`, um servidor MCP por stdio para listar e ler a documentação, o mod e as amostras de código do laboratório. O registro por projeto fica em `.mcp.json`. `claude mcp list` verifica a conexão após a autorização do servidor pelo Claude Code.
