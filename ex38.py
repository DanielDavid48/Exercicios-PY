print('Seja bem vindo!')

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))

if n1 > n2:
    print(f'O número {n1} é maior que {n2}.')

elif n2 > n1:
    print(f'O número {n2} é maior que {n1}.')

else:
    print(f'O número {n1} e {n2} saõ iguais, portanto não existe valor maior!')