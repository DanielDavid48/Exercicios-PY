import os

print('Bem vindo ao convertor de temperaturas!')
print(f'Escolha uma das opções abaixo:{os.linesep}A - para converter celsius para fahrenheit{os.linesep}B - para converter fahrenheit para celsius')
opcao = input('Opção escolhida: ')

# Celsius para fahrenheit


# fahrenheit para celsius


if opcao == 'A':
    temp = float(input('Insira a temperatura em °C: '))
    conversao1 = temp * 1.8 + 32
    print(f'{temp} graus celsius em fahrenheit é {conversao1:.2f} graus fahrenheit.')

elif opcao == 'B':
    tempfa = float(input('Insira a temperatura em °F: '))
    femc = (tempfa - 32)/1.8
    print(f'{tempfa} graus fahrenheit em celsius é {femc:.2f} graus celsius')

else:
    print('Você digitou uma opção inválida!')
