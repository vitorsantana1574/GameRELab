# Elden Ring

| Ferramenta | Uso |
| --- | --- |
| Smithbox | Comparar parâmetros de ataques, NPCs e outros dados. |
| DSAnimStudio e HkbEditor | Estudar animações, eventos e grafos em formatos compatíveis. |
| WitchyBND e DarkScript3 | Abrir cópias de contêineres e examinar eventos. |
| me3 | Organizar mods em um perfil separado de modding offline. [Documentação](https://github.com/garyttierney/me3/blob/main/docs/index.md) |

Comece por uma cópia de trabalho em `projects/elden-ring/local/`. Escolha um ataque, registre o NPC e o ID da animação e compare o intervalo dos eventos com os parâmetros do ataque. Exporte somente as anotações e seus próprios arquivos de projeto. Para teste dentro do jogo, use um perfil separado e faça uma cópia do save antes de carregar alterações.

## Inicialização do Smithbox

Use `scripts/smithbox.ps1` para iniciar o executável Vulkan indicado pelo projeto. O script verifica, antes de abrir o programa, se o usuário atual consegue criar e gravar em `%LOCALAPPDATA%\Smithbox\Configuration`. Essa pasta é usada pelas versões Vulkan e OpenGL já no início da execução. Uma falha de escrita nessa pasta pode aparecer no Windows como a exceção genérica `0xe0434352`. [Smithbox](https://github.com/vawser/Smithbox)
