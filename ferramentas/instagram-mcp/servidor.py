"""MCP stdio. Logs nunca são escritos em stdout; nenhum token é retornado."""
from mcp.server.fastmcp import FastMCP
from mcp.types import ToolAnnotations
import analise
from core import collect

mcp = FastMCP('instagram-moises', instructions='Métricas oficiais locais. null significa ausente. Não atribua causalidade a rankings; confira idade e tamanho da amostra. Nenhuma ferramenta publica ou apaga conteúdo no Instagram.')
read = ToolAnnotations(readOnlyHint=True, destructiveHint=False, openWorldHint=False)

@mcp.tool(annotations=read)
def listar_posts(desde: str, serie: str | None=None) -> list[dict]:
    """Reels publicados desde AAAA-MM-DD, com último snapshot e dados ausentes."""
    return analise.listar_posts(desde,serie)

@mcp.tool(annotations=read)
def metricas_post(id_ou_link: str) -> dict:
    """Métricas acumuladas e evolução de um Reel pelo ID ou permalink."""
    return analise.metricas_post(id_ou_link)

@mcp.tool(annotations=read)
def comparar_series(desde: str) -> dict:
    """Medianas por série/estilo, número de valores válidos e mediana do perfil."""
    return analise.comparar_series(desde)

@mcp.tool(annotations=read)
def top_e_bottom(desde: str, n: int=3) -> dict:
    """Ranking com critério explícito (CTA, compartilhamentos ou alcance)."""
    return analise.top_e_bottom(desde,n)

@mcp.tool(annotations=read)
def conta(desde: str) -> dict:
    """Histórico observado de seguidores e insights diários disponíveis."""
    return analise.conta(desde)

@mcp.tool(annotations=ToolAnnotations(readOnlyHint=False,destructiveHint=False,openWorldHint=True))
def coletar_agora(desde: str | None=None) -> dict:
    """Consulta API oficial (GET), grava novo snapshot apenas local. Pode levar minutos."""
    return collect(desde)

if __name__=='__main__':
    mcp.run(transport='stdio')
