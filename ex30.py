print('Vamos ver se esse número é PAR ou IMPAR?')
n = int(input('Insira um número aqui: '))

# verificando se e par

par = n % 2

if par == 0:
    print(f'O número {n} é par!')

else:
    print(f'O número {n} é impar!')