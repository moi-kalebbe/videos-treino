# Prompt para o Codex: nosso "Windsor" próprio (MCP de métricas do Instagram)

> Cole junto com `prompts/codex-reforco.md` e `prompts/codex-analise-instagram.md`. Leia também `referencias/instagram-analise.md`.
> Se for usar o repositório/ferramenta que "clona" projetos, use-o como **referência de arquitetura e de funcionalidade**, não para copiar código, interface, textos ou marca do Windsor.ai (é produto pago e proprietário). Nome do repositório/ferramenta: <!-- preencher -->

## A ideia
O Windsor.ai é, no fundo, três peças: (1) **conectores** que puxam dados das redes pela API oficial, (2) um **armazém** com o histórico, e (3) um **servidor MCP** que deixa o Claude/Codex perguntar sobre esses dados ("qual Reel teve mais compartilhamento por alcance?"). Para um perfil só (o nosso), dá para fazer isso de graça com a API do Instagram que já usamos para publicar.

Depois, **juntamos com o `sergebulaev/instagram-skills`**: o nosso MCP traz os **números do nosso perfil**; as skills trazem **leitura do nicho, auditoria do perfil e ganchos**. Um agente cruza os dois.

## O que construir (em `ferramentas/instagram-mcp/`, Python)
1. **Coletor** (`coletar.py`)
   - Usa `INSTAGRAM_USER_ID` e `INSTAGRAM_ACCESS_TOKEN` do `.env` (base `https://graph.instagram.com/v23.0`; veja `scripts/publicar-instagram.py`).
   - Puxa posts, insights de cada Reel (`reach`, `views`/`plays`, `likes`, `comments`, `shares`, `saved`, `total_interactions`, `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`), insights da conta (`reach`, `follower_count`, `profile_views`, `accounts_engaged`, `website_clicks`) e a contagem de comentários com a palavra do CTA (`DIAGNÓSTICO` etc.). Métrica que a API não devolver: registra como ausente, não inventa.
   - Grava em **SQLite** (`dados/instagram.db`, fora do git), com data da coleta (para ver a evolução de cada post dia a dia).
   - Liga cada post à série/estilo pelo `calendario.md` e ao roteiro (`roteiros/<slug>.md`: duração, gancho).
2. **Servidor MCP** (`servidor.py`, SDK oficial `mcp` em Python, transporte stdio)
   - Ferramentas:
     - `listar_posts(desde, serie?)` → posts com métricas principais;
     - `metricas_post(id_ou_link)` → tudo de um post + evolução;
     - `comparar_series(desde)` → mediana de alcance, retenção (tempo médio ÷ duração), shares/alcance, saves/alcance e comentários com CTA por série/estilo;
     - `top_e_bottom(desde, n=3)` → melhores e piores, com os números;
     - `conta(desde)` → seguidores, alcance e visitas ao perfil por dia;
     - `coletar_agora()` → roda o coletor.
   - Só leitura: o MCP nunca publica nem apaga nada.
   - Registrar no Codex (`~/.codex/config.toml`) e no Claude Code (`claude mcp add instagram-moises -- python3 <caminho>/servidor.py`). Mostrar ao dono o comando antes de rodar.
3. **Painel simples** (`painel.html`, gerado pelo coletor): uma página estática com os gráficos principais (alcance por post, retenção, shares/saves, CTA), sem servidor. Opcional.
4. **Coleta automática:** LaunchAgent diário às 7h (padrão de `agendamentos/`), carregado só depois do OK do dono.

## Juntar com o `instagram-skills`
- Instale: `codex plugin marketplace add sergebulaev/instagram-skills` e `codex plugin add instagram-skills@instagram-skills`. Leia o código antes; não passe o nosso token para ele.
- Crie um fluxo (skill nossa, `skills/analise-semanal/`) que:
  1. chama o nosso MCP (`comparar_series`, `top_e_bottom`);
  2. chama as skills de auditoria de perfil e "o que funciona no nicho" (Apify custa por uso: avise o dono antes e use os créditos grátis);
  3. escreve `analises/instagram/AAAA-MM-DD.md`: o que repetir, o que parar e o próximo vídeo sugerido, ligado ao `calendario.md`, em linguagem de dono.

## Regras
- Repo público: **nada** de token, banco SQLite, nome ou texto de comentário de seguidor no git. Só código e relatórios com contagens.
- Erro de permissão: o token pode precisar do escopo `instagram_business_manage_insights`. Explique ao dono o que pedir no app da Meta; não contorne.
- Não copiar código, layout nem textos do Windsor.ai.
- Teste primeiro com os posts já publicados (Plantão IA 01, A Virada 01) e mostre ao dono antes de agendar.

## Entrega
- `ferramentas/instagram-mcp/` com coletor, servidor MCP e README de instalação.
- MCP funcionando no Codex e no Claude Code (o dono testa perguntando "qual série está indo melhor?").
- Primeiro relatório em `analises/instagram/`.

## O que eu quero agora
<!-- Ex.: "Monta a primeira versão, conecta no Codex e me mostra o relatório da semana." -->
