# League of Legends

O script do laboratório consulta os dados públicos de campeões no Data Dragon em português brasileiro. A lista de versões vem da Riot e o resultado identifica o patch usado.

```powershell
python projects/league-study/dragon.py Ahri
```

Para medir uma habilidade em uma gravação, registre o patch, FPS, quadro inicial e quadro final. Divida a diferença entre os quadros pelo FPS e guarde a unidade de tempo. Use replays e gravações para revisar as medições.

Para estatísticas de partidas, siga os requisitos de cadastro e de uso dos endpoints documentados. A política da Riot trata aplicativos que concedem vantagem competitiva e restringe leitura direta de memória. [Data Dragon e API](https://developer.riotgames.com/docs/lol) · [Aplicativos de terceiros](https://support.riotgames.com/en-us/riot/events/third-party-applications)
