print('Calculadora de fatorial ><><')

n = int(input('Insira um número: '))
cont = b = n
while cont != 1:
    cont -= 1
    b = b * cont
    print(b)