"""Teste de integração real via stdio: inicialização, catálogo e cinco consultas."""
import asyncio
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params=StdioServerParameters(command=sys.executable,args=[str(Path(__file__).with_name('servidor.py'))])
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            names={t.name for t in (await session.list_tools()).tools}
            expected={'listar_posts','metricas_post','comparar_series','top_e_bottom','conta','coletar_agora'}
            assert names==expected,names
            for name in sorted(expected-{'coletar_agora'}):
                args={'id_ou_link':'https://www.instagram.com/reel/DepsxCiEzF1/'} if name=='metricas_post' else {'desde':'2026-10-12'}
                result=await session.call_tool(name,args)
                assert not result.isError,(name,result)
                print('OK',name)
            print('OK catálogo: seis ferramentas; coleta já validada pela CLI, não repetida neste teste.')

if __name__=='__main__': asyncio.run(main())
