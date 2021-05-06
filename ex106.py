import time

c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7;40m'
     )

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    time.sleep(2)
    
def titulo(msg, cor=0):
    tam = len(msg)
    print('=' * tam)
    print(f'{msg}')
    print('=' * tam)
    print(c[0], end='')
    
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PY HELPER', 2)
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo', 1)