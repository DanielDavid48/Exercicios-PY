import time
from random import randint

print('Olá, que bom tê-lo por aqui :D')
time.sleep(1)

lista = []
def sorteio():
    """
    teste
    """
    print('Sorteando 5 valores:', end=' ')
    for x in range(0, 5):
        n = randint(1, 100)
        print(f'\033[33m{n}\033[m', end=', ')
        time.sleep(0.5)
        lista.append(n)
    print()

def somapar():
    somador = 0
    for items in lista:
        if items % 2 == 0:
            somador += items
    print('Os números pares sorteados são:', end=' ')
    for i in lista:
        if i % 2 == 0:
            print(f'\033[33m{i}\033[m', end=', ')
            time.sleep(0.5)
    print()
    print(f'E a soma dos números \033[36mpares\033[m resulta em \033[36m{somador}\033[m.')

sorteio()
somapar()

help(sorteio)