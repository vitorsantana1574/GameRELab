# Arquitetura do laboratório

| Diretório | Conteúdo |
| --- | --- |
| `projects/` | Código e projetos de estudo separados por jogo, além da amostra própria de análise de software. |
| `scripts/` | Instalação das ferramentas, comandos de compilação e verificações. |
| `manifests/` | Versões e fontes dos pacotes portáteis para Windows. |
| `tools/` | Ferramentas portáteis extraídas por versão. |
| `sandbox/` | Cache do Gradle, resultados temporários e configurações locais dos agentes. |
| `backups/` | Cópias locais de trabalho e saves. |
| `reports/` | Estado dos testes e relatórios resumidos. `reports/local/` recebe dados da máquina. |

A instalação portátil reutiliza Python, Git, editores e launchers existentes. Java 21 atende o Minecraft 1.21.1 e Java 25 atende o Ghidra 12.2. Os scripts selecionam os JDKs na pasta do projeto.
