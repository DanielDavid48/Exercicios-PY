print('\033[32mSeja bem vindo à Davids E-commerce\033[m')
nome = str(input('Me informe seu nome: '))
print(f'\033[32Prazer em te conhecer {nome}!\033[m')
valor = int(input('Insira o valor do produto: R$'))
print("""Formas de pagamento: 
1 - À vista (dinheiro ou cheque) 
2 - À vista no cartão
3 - Em até 2x no cartão
4 - 3x ou mais no cartão""")
opcao = int(input('Digite o número da opção aqui: '))

# avista dinheiro e cheque

a_vista = 10 * valor
a_vista1 = a_vista / 100
a_vista2 = valor - a_vista1

# cartao 1x
cartao = 5 * valor
cartao1 = cartao / 100
cartao2 = valor - cartao1

# ate 2x
ate2vezes = valor

# calculando prcelas 2x
parc2 = ate2vezes / 2

# 3x ou mais
vezes3oumais = 20 * valor
vezes3oumais1 = vezes3oumais / 100 
vezes3oumais2 = vezes3oumais1 + valor
totalparc = int(input('Quantas vezes quer parcelar: '))
parcela = vezes3oumais2 / totalparc

if opcao == 1:
    print(f'{nome}, o produto ficará em R${a_vista2:.2f} reais.')

elif opcao == 2:
    print(f'{nome}, o produto ficará em R${cartao2:.2f} reais.')

elif opcao == 3:
    print(f"""{nome}, ficarão 2 parcelas de R${parc2:.2f} reais.
O produto ficará em R${ate2vezes:.2f} reais.""")

elif opcao == 4:
    print(f"""{nome}, ficará {totalparc} parcelas de R${parcela:.2f} reais. 
O produto ficará em R${vezes3oumais2:.2f} reais.""")

else:
    print('\033[31mVocê digitou uma opção inválida!\033[m')