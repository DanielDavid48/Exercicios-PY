
def fatorial(num=1):
    """
    > Calcula o fatorial de um numero
    :show: Se show for igual a 's' Mostra o processo de fatoração
    senaão, esconde o processo de fatoração e apenas imprimie o resultado
    
    : for dentro do for: serve para imprmir o ultimo x como =, sendo assim
    numero x numero = resultado.
    """
    if show == 's':
        f = 1
        cont = 0
        conta = n - 1
        for c in range(n, 0, -1):
            print(f'\033[33m{c}\033[m', end=' ')
            for e in range(1):
                if cont == conta:
                    break
                print('x', end= ' ')
            cont += 1
            f *= c   
        print(f'= \033[36m{f}\033[m')
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c   
        print(f'o resultado da fatoração é = \033[36m{f}\033[m')
        
def line():
    print('='*50)
    
n = int(input('Quer fatorar qual número: '))
show = input('Quer mostrar o processo [s/n]: ').lower()

line()
fatorial()
line()
