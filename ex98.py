import time

def contador(inicio, fim, passo):
    if passo == 0 and fim > inicio:
        passo += 1
    elif fim < 0 or fim < inicio and passo == 0:
        passo = -passo + -1
    elif fim < 0 or fim < inicio and passo > 0:
        passo = -passo 
    
    print(f'\033[33mContando de {inicio} ao {fim}, pulando de {passo} em {passo}\033[m')
    for contador in range(inicio, fim, passo):
        print(f'{contador}', end=', ')    
    print()
    
def linhas():
    print('='*17)
    print('\033[33mAgora é sua vez!\033[m')
    print('='*17)

contador(0, 10, 1)
contador(10, 0, -2) 
linhas()
contador(int(input('\033[32mInsira o começo:\033[m ')), int(input('\033[32mInsira o fim:\033[m ')), int(input('\033[32mInsira os passos:\033[m ')))