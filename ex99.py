import time

def maior(lista):
    print('\033[33m=\033[m'*50)
    print('Analisando os valores', end= ' ')
    for item in lista:
        print(f'\033[36m{item}\033[m', end= ', ')
        time.sleep(0.5)
    print()
    print('\033[33m=\033[m'*50)
    print(f'Ao todo, foram passados {len(lista)} valores.')
    print(f'O maior valor desta lista foi {max(lista)}')
    print(f'E a soma destes valores resulta em {sum(lista)}.')
    time.sleep(1)
    
lista = []
continuar = ''

while continuar == '':
    n = int(input('Insira um número: '))
    lista.append(n)
    continuar = input('Para continuar: \033[33mENTER\033[m | Para sair: \033[m0\033[m  >= Opção: ')
    while continuar not in "''0":
        print('\033[31mOpção inválida!\033[m')
        continuar = input('Para continuar: \033[33mENTER\033[m | Para sair: \033[33m0\033[m >= Opção: ') 

maior(lista)