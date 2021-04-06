import os

print('Bem vindo ao DOLARIZEI')
print('Escolha uma opção para continuarmos!')
print(f'A para ver a cotação do dólar{os.linesep}B para ver a cotação do euro{os.linesep}C para saber quantos dólares você pode comprar{os.linesep}D para ver quantos euros você pode comprar.')
opcao = input('Opção: ')

cotacao = 'R$5,50'
euro = 'R$6,65'

if opcao == 'A':
    print(f'A cotação do dólar é {cotacao} por dólar.')

elif opcao == 'B':
    print(f'A cotação do euro é {euro} por euro.')

elif opcao == 'C':
    c = float(input('Quantos reais você tem: R$'))
    conta = c / 5.50
    print(f'Com os R${c} reais que você tem, atualmente você poderá comprar US${conta:.2f} dólares')

elif opcao == 'D':
    e = float(input('Quantos reais você tem: R$'))
    conta_euro = e / 6.65
    print(f'Com os R${e} reais que você tem, atualmente você poderá comprar €{conta_euro:.2f} euros')

else:
    print('Você escolheu uma opção inválida!')
