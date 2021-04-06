from colorama import Fore, Back, Style
import os

print('Seja bem vindo ao Banco do POVO!')

nome = str(input('Me informe seu nome por gentileza: '))
print(f'Prazer em te conhecer {nome}')

print(f'{nome}, qual é o valor da casa? OBS: Não coloque pontos ou vírgulas!')
valor_casa = float(input('Valor da casa: R$ '))
print(f'Ok {nome}, então o valor da casa é {valor_casa}.... Anotei aqui.')
print(f'{nome}, qual é o seu salário atual? OBS: Não coloque pontos ou vírgulas!')
salario = float(input('Meu salário atual é: R$ '))
print('ok, agora uma última informação, em quantos anos quer pagar essa casa?')
anos = int(input('Digite aqui: '))

# convertendo anos em meses
anos_meses = anos * 12

# calculando as parcelas
parcela = valor_casa / anos_meses

# calculando se excede os 30% do salario
salario1 = 30 * salario
salario2 = salario1 / 100

if parcela > salario2:
    print(f'\033[31m{nome}\033[m, \033[31minfelizmente o valor da parcela mensal excede 30% do seu salário, {os.linesep}por isso, estamos negando seu empréstimo!\033[30m') 
    print('\033[m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\033[m')
    print('\033[31mVeja um resumo sobre o RECUSAMENTO:\033[m') 
    print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
    print(f'>>> O seu salário atual é R${salario:.2f} reais.{os.linesep}>>> 30% do seu salário é igual a R${salario2:.2f}.{os.linesep}>>>> O nosso banco, não aceita parcelamentos que excedam 30% do salário.{os.linesep}>>> Você pode tentar aumentar os anos à pagar ou encontrar uma residência com um valor menor.')
    print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')

elif parcela <= salario2:
    print(f"""\033[32m{nome}, o seu empréstimo foi aprovado, o valor das 
parcelas ficará em R${parcela:.2f} reais mensais!\033[m""")