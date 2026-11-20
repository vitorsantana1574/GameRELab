# Codex

Inicie o Codex na raiz do repositório, onde ele encontra `AGENTS.md`. Use `rg --files projects` para listar o código e `rg -n 'class |onInitialize' projects` para localizar classes e inicializadores Java.

O servidor MCP do GameRELab oferece listagem e leitura de guias e projetos de exemplo por stdio. Como as entradas da CLI são configuradas por usuário, `scripts/test-mcp.ps1` usa um perfil isolado em `sandbox/` para registrar e verificar o servidor no Codex. O mesmo script verifica o perfil de projeto do Claude Code e faz chamadas MCP diretamente, com Python.
