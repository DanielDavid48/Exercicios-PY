print('Seja bem vindo a BUSER')

usuario = str(input('Me diga seu nome: '))
print(f'Prazer em te conhecer {usuario}!')

# distancia
print(f'{usuario}, e qual a distância da sua viajem em KM?')
distancia = float(input('A distância é (informe somente números):  '))

# calculando a passagem
if distancia >= 200:
    conta1 = distancia * 0.45
    print(f'{usuario}, a sua viajem fica em R${conta1:.2f} reais.')

else:
    conta2 = distancia * 0.50
    print(f'{usuario}, sua viajem fica em R${conta2:.2f} reais.')
