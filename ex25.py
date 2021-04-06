print('Seja bem vindo')
nome = input('Insira seu nome: ')

# convertendo a string nome para minuscula

mi = nome.lower()

# procurando a string Silva na string nome

nome1 = mi.find('silva')

if nome1 >= 1:
    print(f'No nome {nome}, há o sobrenome Silva.')

else:
    print(f'No nome {nome}, não há o sobrenome Silva.')