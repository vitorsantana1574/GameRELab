# GameRELab

Laboratório gratuito para Windows. Inclui um mod de exemplo para Minecraft, uma amostra própria para análise estática e ferramentas para estudar jogos e desenvolver mods.

| Área | Material |
| --- | --- |
| Instalação e ferramentas | [Ferramentas](docs/FERRAMENTAS.md) · [Arquitetura](docs/ARQUITETURA.md) |
| Minecraft Java | [Fabric 1.21.1 e Cobblemon](docs/MINECRAFT.md) |
| Elden Ring | [Modding offline](docs/ELDEN-RING.md) |
| Baldur’s Gate 3 | [Toolkit oficial](docs/BALDURS-GATE-3.md) |
| League of Legends | [Data Dragon e estudo de replays](docs/LEAGUE-OF-LEGENDS.md) |
| Agentes | [Claude Code](docs/CLAUDE-CODE.md) · [Codex](docs/CODEX.md) |
| Validação | [Resultados dos testes](reports/TESTES.md) · [Situação da implantação](reports/RELATORIO_FINAL.md) |

No PowerShell, na raiz do repositório:

```powershell
python scripts/install-tools.py jdk21 gradle jdk25 ghidra
.\scripts\minecraft.ps1 build
.\scripts\test-ghidra.ps1
python projects/league-study/dragon.py Ahri
```

O código e os exemplos originais deste repositório usam a [licença MIT](LICENSE). Ferramentas, jogos e dependências têm suas próprias licenças.
