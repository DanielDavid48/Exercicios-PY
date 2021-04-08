from random import choice

print('\033[32mSeja bem vindo!\033[m')
print('\033[33mTente advinhar um número que a máquina irá escolher entre 0 e 10.\033[m')

lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

escolha_maquina = choice(lista)
escolha_usuario = input('Tente adivinhar: ')

cont = 1
while escolha_usuario != escolha_maquina:
    escolha_usuario = input('Tente novamente: ')
    cont += 1

print(f'\033[32mApós {cont} tentavivas, você conseguiu acertar o número escolhido pela máquina, que é {escolha_maquina}!\033[m')