"""Gera LaunchAgent diário, sem carregá-lo. Ative somente após aprovação."""
import plistlib
from core import LOCAL

if __name__=='__main__':
    path=LOCAL/'dados/com.moiseskalebbe.instagram-metricas.plist'
    path.parent.mkdir(parents=True,exist_ok=True)
    job={'Label':'com.moiseskalebbe.instagram-metricas',
         'ProgramArguments':[str(LOCAL/'.venv/bin/python'),str(LOCAL/'coletar.py')],
         'WorkingDirectory':str(LOCAL),
         'StartCalendarInterval':{'Hour':7,'Minute':0},
         'EnvironmentVariables':{'TZ':'America/Sao_Paulo','PATH':'/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin'},
         'StandardOutPath':str(LOCAL/'dados/coleta.log'),
         'StandardErrorPath':str(LOCAL/'dados/coleta-erro.log'),
         'ProcessType':'Background'}
    path.write_bytes(plistlib.dumps(job));path.chmod(0o600)
    print('Preparado, NÃO carregado:',path)
