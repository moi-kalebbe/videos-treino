# Prompt para o Codex: análise do Instagram (o que está dando certo)

> Cole este arquivo inteiro no Codex, junto com o `prompts/codex-reforco.md`. Leia antes `referencias/instagram-analise.md`: as duas referências que o dono subiu (conector **Windsor.ai** no Claude e o repositório **sergebulaev/instagram-skills**, que tem plugin para o Codex).

## Objetivo
Responder toda semana, com dados do próprio perfil **@moiseskalebbe**: **qual série, estilo, gancho e tema está funcionando**, para decidir o próximo vídeo. O dono quer ver as métricas e o que repetir, não um painel bonito sem conclusão.

## O que já existe (não refazer)
- Acesso à API do Instagram (Instagram Login, app "appmoi"): `INSTAGRAM_USER_ID` e `INSTAGRAM_ACCESS_TOKEN` no `.env` (nunca no git). Base `https://graph.instagram.com/v23.0`. Veja `scripts/publicar-instagram.py` para o jeito de carregar o `.env` e chamar a API.
- `calendario.md`: cada post publicado tem data, série (Plantão IA, A Virada, Caso Real, IA por Setor, Dossiê) e link do Reel. É a "chave" para ligar métrica a série/estilo.
- `roteiros/<slug>.md`: gancho, efeitos, duração e estilo de cada vídeo.

## Ferramentas que o dono trouxe (avaliar primeiro)
- **sergebulaev/instagram-skills** (MIT): instale no Codex (`codex plugin marketplace add sergebulaev/instagram-skills` + `codex plugin add instagram-skills@instagram-skills`) e use para **auditoria do perfil**, "o que está funcionando no nicho" (Apify, custo por uso: avise antes) e ganchos alternativos. Leia o código antes de dar qualquer token.
- **Windsor.ai** (conector do claude.ai, pago com teste grátis): caminho sem código para o dashboard. Só se o dono quiser pagar; o script abaixo faz o essencial de graça.
- O relatório final pode juntar as duas coisas: **nossos números** (script abaixo) + **leitura do nicho e do perfil** (skills).

## O que construir
1. **`scripts/analise-instagram.py`**
   - Puxa os posts (`/{user-id}/media?fields=id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count`) com paginação.
   - Para cada Reel, puxa os insights (`/{media-id}/insights?metric=...`). Comece por: `reach`, `views` (ou `plays`, conforme a versão), `likes`, `comments`, `shares`, `saved`, `total_interactions`, `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`. Se uma métrica não existir na versão da API, registre e siga (não quebre).
   - Puxa os insights da conta: `reach`, `follower_count`, `profile_views`, `accounts_engaged`, `website_clicks` (período diário/semana), e demografia de seguidores se a permissão permitir.
   - Lê os **comentários** de cada post e conta quantos têm a palavra do CTA (`DIAGNÓSTICO`, `RELATÓRIO`, etc.). Esse é o número que mais importa para o negócio.
   - Liga cada post ao `calendario.md` (pelo link/permalink ou pela data) para saber a série e o estilo, e ao roteiro para pegar duração e gancho.
   - Guarda o histórico em `analises/instagram/dados/AAAA-MM-DD.json` (sem token, sem dado pessoal de quem comentou: só contagens).
2. **Métricas derivadas (por post e por série)**
   - Retenção: `avg_watch_time / duração do vídeo` (quanto do vídeo a pessoa assiste em média).
   - Taxa de compartilhamento e de salvamento por alcance (`shares/reach`, `saved/reach`): compartilhar = alcance novo; salvar = utilidade.
   - Conversão do CTA: `comentários com a palavra / alcance`.
   - Seguidores ganhos na semana do post (aproximação pelo `follower_count` diário).
   - Comparar com a **mediana do perfil** (não com média: um viral distorce).
3. **Relatório semanal em `analises/instagram/AAAA-MM-DD.md`**
   - Top 3 e bottom 3 da semana, com o porquê provável (gancho, duração, tema, estilo), citando os números.
   - Tabela por série/estilo: alcance mediano, retenção, shares, saves, comentários com CTA.
   - "O que repetir" e "o que parar", em no máximo 5 linhas cada, em linguagem de dono (sem jargão).
   - Sugestão do próximo vídeo baseada nos dados, ligada ao `calendario.md`.
   - Um gráfico simples por métrica principal (PNG com matplotlib, ou HTML estático), opcional.
4. **Rodar sozinho:** um LaunchAgent toda segunda às 8h (mesmo padrão de `agendamentos/`), salvando o relatório e avisando o dono. Comitar só o relatório e o script, nunca o `.env`.

## Regras
- **Honestidade com número:** se a API não devolve uma métrica, diga que não tem; nunca estime como se fosse dado. Amostra pequena (menos de ~5 posts por série) é "indício", não conclusão.
- **Privacidade:** não salvar nome, usuário ou texto de comentário de seguidores no repo (o repo é público). Só contagens e palavras-chave.
- **Token:** se der erro de permissão, o token pode precisar do escopo `instagram_business_manage_insights`. Explique ao dono o que pedir no app da Meta; não tente contornar.
- **Créditos:** nada aqui gasta ElevenLabs.
- Teste primeiro com os posts já publicados (Plantão IA 01, A Virada 01) e mostre o relatório ao dono antes de agendar.

## Entrega esperada
- `scripts/analise-instagram.py` funcionando, com `--desde AAAA-MM-DD`.
- `analises/instagram/` com o primeiro relatório.
- LaunchAgent pronto (carregado só depois do OK do dono).
- Uma linha no `CLAUDE.md`/`AGENTS.md` dizendo onde fica a análise e quando roda.

## O que eu quero agora
<!-- Ex.: "Faz a primeira versão e me mostra o relatório da semana." -->
