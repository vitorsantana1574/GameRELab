# Minecraft Java e Cobblemon

O exemplo usa Fabric Loader 0.18.4, Minecraft Java 1.21.1 e JDK 21. Essa combinação coincide com a instância COBBLEVERSE encontrada nesta implantação, com Cobblemon Fabric 1.7.3. Há também [um modpack oficial Fabric](https://modrinth.com/modpack/cobblemon-fabric/version/1.7.3) para a mesma versão do jogo.

```powershell
python scripts/install-tools.py jdk21 gradle
.\scripts\minecraft.ps1 build
.\scripts\minecraft.ps1 runClient
```

O JAR final sai em `projects/minecraft/build/libs/`. No cliente de desenvolvimento, entre em um mundo e execute `/gamerelab` para obter `GameRELab pronto.`. O exemplo só depende de Fabric API e pode ser colocado em um perfil de teste com Cobblemon. O código fica em `projects/minecraft/src/`.

## Alterar Cobblemon

Comece por um datapack para alterações suportadas pelos dados do jogo. Para mecânicas que exigem Java, mantenha um add-on Fabric separado e use a API do mod ou mixins pontuais conforme o caso. Consulte a versão e a licença dos [projetos oficiais do Cobblemon](https://gitlab.com/cable-mc) antes de redistribuir alterações. JARs de loaders diferentes exigem versões próprias do mod.

## Multiplayer com Radmin VPN

Use a mesma versão do Minecraft, Fabric Loader, Cobblemon, Fabric API e mods exigidos em ambos os lados. Use a distribuição de servidor do próprio modpack, quando disponível. O `runServer` do exemplo serve ao mod de teste e inicia sem a lista de mods do COBBLEVERSE. Cada jogador mantém sua própria conta e conecta ao IP Radmin do anfitrião, normalmente na porta TCP 25565.

Teste primeiro um cliente local. Em seguida, valide a conexão do amigo pelo Radmin com o servidor ativo e compare a lista de mods se o handshake falhar. Use uma cópia do mundo para testes de alteração do modpack.
