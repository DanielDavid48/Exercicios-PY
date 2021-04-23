numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

escolha_user = int(input('Digite um número entre 0 e 20: '))
while escolha_user > 20:
    escolha_user = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[escolha_user]}.')
continur = input('Quer continuar [s/n]: ').lower()

while continur == 's':
    escolha_user = int(input('Digite um número entre 0 e 20: '))
    while escolha_user > 20:
        escolha_user = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {numeros[escolha_user]}.')
    continur = input('Quer continuar [s/n]: ').lower()
    
print('Programa finalizado!')