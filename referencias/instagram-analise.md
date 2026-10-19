# Referências: análise do Instagram com IA (Notas Rápidas, 18/10/2026)

O dono subiu nas Notas Rápidas dois Reels sobre usar o Claude para analisar e cuidar do Instagram. Foram baixados (refs 16 e 17, brutos fora do git), mas só registrados aqui em 19/10/2026.

## Ref 16 · Lucas Cunha · "Conectei o Claude no meu Instagram"
- Link: https://www.instagram.com/reel/Dbd8BDvJH6x/
- **O que mostra:** no claude.ai → Configurações → Conectores → **Navegar conectores** → busca **Windsor.ai** (aparece em "Anthropic e Parceiros") → autoriza ("Application Access Request") → no Windsor.ai seleciona **Instagram** (e sites) e loga a conta → volta ao Claude, confirma o conector e cola um prompt. O Claude monta um **dashboard do perfil** com o que melhorar e um plano passo a passo.
- **Promessa:** "+14 mil seguidores em 28 dias" (não comprovado; CTA "comenta emoji que eu mando o prompt").
- **O que agrega:** o caminho sem código: conector Windsor.ai (MCP de dados de marketing: Instagram, Meta Ads, Google Ads etc.) + Claude lendo as métricas reais. Windsor.ai é serviço pago (tem teste grátis): conferir custo antes.

## Ref 17 · Filipe Martinelli · "Faz o Claude cuidar do seu Instagram"
- Link: https://www.instagram.com/reel/DenO45zRVz6/
- **Repositório:** [sergebulaev/instagram-skills](https://github.com/sergebulaev/instagram-skills) (MIT, ~500 estrelas). **9 skills** para Claude Code e Codex: legenda e gancho de Reels na voz da marca, hashtags, carrossel, plano da semana, "o que está funcionando no meu nicho" (dados reais via **Apify**), **otimização do perfil**, e remoção de "cara de IA" do texto. Tudo passa por aprovação antes de publicar (publica via Publora, opcional).
- **Instalar no Codex:** `codex plugin marketplace add sergebulaev/instagram-skills` e `codex plugin add instagram-skills@instagram-skills`. No Claude: Skills → Add from GitHub → `sergebulaev/instagram-skills`.
- **O que agrega:** auditoria do perfil e análise do nicho prontas; geração de ganchos alternativos para os nossos Reels.

## Como isso entra no nosso fluxo
- **Métricas do nosso perfil** (o que deu certo por série e estilo): o mais barato é o nosso próprio script na API do Instagram (já temos o token), ver [prompt do Codex](../prompts/codex-analise-instagram.md). O Windsor.ai é a alternativa sem código, paga.
- **Nicho, ganchos e perfil:** o `instagram-skills` (grátis, MIT; o Apify tem custo por uso).
- Cuidado: não colar token em skill de terceiro sem ler o código; o repo pede `.env` próprio.
