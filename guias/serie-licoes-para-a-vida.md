# Lições para a Vida — série diária de Stories

## Fonte e conteúdo

- O dono recebe por email um PDF com três lições de desenvolvimento pessoal por dia. Produzir **um Story independente para cada lição** a partir desse PDF.
- Usar somente as ideias presentes no PDF como fonte do roteiro. Conferir se a interpretação corresponde ao texto e indicar o livro/autor quando constarem no PDF. Paráfrases não são citações literais.
- Criar situações comuns, hipotéticas e úteis para a maioria das pessoas. **Não usar** anotações de estudo, conversas, relatos, negócios, família ou exemplos pessoais do dono, mesmo que estejam disponíveis em outro lugar. Se um exemplo do PDF parecer pessoal ou específico, generalizá-lo.
- Não afirmar nem insinuar que o dono estudou, viveu ou recomenda algo por experiência própria. O recebimento e a publicação do PDF não dependem de confirmar se ele estudou.
- Texto curto e falado de modo natural: uma ideia, um exemplo geral e uma ação simples por Story. Evitar promessas de resultado e atribuições que o PDF não sustente.

## Identidade do vídeo

- Usar a voz clonada do dono já configurada em `guias/voz-e-audio.md`, gerada em blocos pelo script existente. O `.env` com a chave do ElevenLabs é local e não deve ir ao Git. Se estiver ausente, preparar roteiro e visual, mas não apresentar voz provisória como versão final.
- O dono quer seu avatar em **todo vídeo animado da série**. Usar somente uma foto ou um avatar que ele tenha confirmado ser seu. A pasta `producao/apresentador/` continha rostos incorretos e suas cinco imagens foram removidas em `73d4b7f`.
- Priorizar avatar real reutilizável (imagem ou recorte 2D) com movimentos locais simples, junto com cenas e tipografia animadas. Isso evita gerar sincronização labial paga para cada Story. Se um vídeo realmente pedir boca sincronizada, estimar os créditos antes de gerar.
- Enquanto não houver um arquivo visual confirmado do dono, **não publicar nem chamar o personagem genérico do piloto de avatar dele**. Manter fotos, bases de rosto, voz e vídeos finais fora do Git público conforme `.gitignore`.

## Cadência e publicação

- Há uma proposta inicial de distribuir os três Stories ao longo do dia (por exemplo, 6h, 12h e 18h, no fuso de São Paulo), ainda sem configuração de publicação automática.
- Não assumir que apagar Stories antigos aumenta o engajamento. Validar a regra atual da plataforma e medir o resultado antes de automatizar exclusões. Cada Story deve funcionar sozinho.
- Antes de publicar: revisar fidelidade ao PDF, exemplos genéricos, identidade do avatar, pronúncia da voz, duração, legibilidade e custo estimado.

## Ponto de partida

- `producao/licoes-para-a-vida-01/` contém um piloto técnico com voz provisória e personagem ilustrado genérico. O MP4 e o áudio não são versionados.
- Próximo passo: obter do dono um arquivo de foto/avatar **confirmado como seu**, localizar o `.env` apenas no dispositivo autorizado, adaptar o piloto a uma das três lições de um PDF real e então avaliar o resultado antes de montar a rotina diária.
