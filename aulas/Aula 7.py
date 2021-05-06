#Ordem de precedência: 1 (); 2 **; 3 * / // %; 4 + -;

# Desafio 1: Faça um programa que leia um número inteiro e mostra na tela o seu sucessor e o seu antecessor.

#n1 = int(input('Digite um número:'))
#conta1 = n1 - 1
#conta2 = n1 + 1
#print(f'O antecessor de {n1} é {conta1} e o sucessor é {conta2}')

#####################################################################################################################3

# Desafio 2: crie um algorítmo que leia um número e mostre  o seu dobro, triplo e raiz quadrada.

#n1 = int(input('Digite um número:'))
#conta1 = n1 * 2
#conta2 = n1 * 2 + n1
#conta3 = n1 ** (1/2)
#print(f'O dobro do seu número {n1} é {conta1}, o triplo do seu número {n1} é {conta2} e a raiz quadrada é {conta3}')

########################################################################################################################

# Desafio 3: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#from typing import Type

#nota1 = float(input('Insira sua nota 1:'))
#nota2 = float(input('Insira sua nota 2:'))
#nota3 = float(input('Insira sua nota 3:'))
#nota4 = float(input('Insira sua nota 4:'))
#nota5 = float(input('Insira sua nota 5:'))
#conta = (nota1 + nota2 + nota3 + nota4 + nota5)/5
#if conta >= 5:
    #print(f'A sua média é {conta}')
    #print('Parabéns, você foi aprovado')

#else:
    #print('Infelizmente você foi reprovado.')

###################################################################################################################

# Desafio 4: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

#print('Converta metros para centímetros ou milimetros')


#opcao = input('Coloque mm pra milimetros e cm para centimetros:')
#n1 = float(input('Insira um valor em metros:'))

#conta1 = n1 / 0.010000
#conta2 = n1 / 0.0010000


#if opcao == 'cm':    
    #print(f'{n1} metros convertido em centímetros é {conta1} centímetros')

#if opcao == 'mm':
    #print(f'{n1} metros convertido em milimetros é {conta2} milimetros')

######################################################################################################################

# Desafio 5: escreva um sistema que leia um número inteiro qualquer e mostre na tela a sua tabuada.

#print('Bem vindo ao TABUADA SIMPLIFICADA')
#t = int(input('Insira um número ao qual deseja descobrir sua tabuada:'))

#t0 = t * 0
#t1 = t * 1
#t2 = t * 2
#t3 = t * 3
#t4 = t * 4
#t5 = t * 5
#t6 = t * 6
#t7 = t * 7
#t8 = t * 8
#t9 = t * 9
#t10 = t * 10

#print(f'A tabuada do número {t} é:')
#print(f'{t0}')
#print(f'{t1}')
#print(f'{t2}')
#print(f'{t3}')
#print(f'{t4}')
#print(f'{t5}')
#print(f'{t6}')
#print(f'{t7}')
#print(f'{t8}')
#print(f'{t9}')
#print(f'{t10}')

#################################################################################################################3

# Desafio 6: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dolares ela pode comprar considerando US1,00 = R$5,50

#print('Bem vindo ao DOLARIZEI')
#print('Escolha uma opção para continuarmos!')
#print('Escolha A para ver a cotação do dólar e B para saber quantos dólares você pode comprar')

#opcao = input('Opção: ')

#cotacao = 'R$5,50'



#if opcao == 'A':
    #print(f'A cotação do dólar é {cotacao}')

#elif opcao == 'B':
    #c = float(input('Quantos reais você tem: '))
    #conta = c * 5.50
    #print(f'Com os {c} reais que você tem, atualmente você poderá comprar {conta:.2f} dólares')

#else:
    #print('Você escolheu uma opção inválida!')

######################################################################################################################## 

# Desafio 7: Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de de 2m².

#alt = float(input('Insira a altura da parede em metros:'))
#largura = float(input('Insira a largura da parede em metros:'))

#area = alt * largura

# 1L de tinta pintam 2m quadrados de parede
#qt_tinta = area / 2


#print(f'A sua área é {area}m² e você precisará de {qt_tinta}L de tinta para pintar a parede por completo')

########################################################################################################################

# Desafio 8: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, Com 5% de desconto

#print('Bem vindo, vamos calular o desconto')
#v = float(input('Insira o valor do produto:'))

#5% de desconto. Porcentagem é número/100. 5% = 5/100, ou tbm 0,05


#valor_com_desconto = v - (v * 5 / 100)

#print(f'O valor do produto é R${v}, mas como você é novo por aqui te daremos 5% de desconto, o preço a ser pago é R$ {valor_com_desconto:.2f}')

#######################################################################################################################

# Desafio 9: Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

#salario_inicial = float(input('Insira seu salário atual: R$'))

#aumento = salario_inicial * 0.15
#conta = aumento + salario_inicial

#print(f'O seu salário inicial é de {salario_inicial}, com o aumento, ele subirá para: R${conta}')

#####################################################################################################################

# Desafio do matew bibolao: Faça um programa que  diferencie 5 clientes. Cliente novo recebe 5% de desconto, cliente entre 1 a 6 meses recebe 10%, cliente de 7 a 12 recebe 12% de desconto.


welcome = input('Bem-vindo, cliente 1, primeiro, conte-me qual o seu nome por gentileza: ')
welcome2 = input('Bem-vindo, cliente 2, primeiro, conte-me qual o seu nome por gentileza: ')
welcome3 = input('Bem-vindo, cliente 3, primeiro, conte-me qual o seu nome por gentileza: ')
welcome4 = input('Bem-vindo, cliente 4, primeiro, conte-me qual o seu nome por gentileza: ')
welcome5 = input('Bem-vindo, cliente 5, primeiro, conte-me qual o seu nome por gentileza: ')

print(f'Que ótimo lhe ver por aqui {welcome}, {welcome2}, {welcome3}, {welcome4}, {welcome5}, preciso apenas de mais um dado para podermos dar prosseguimento...')


cliente1 = int(input(f'{welcome} Você é nosso cliente a quantos meses?'))
cliente2 = int(input(f'{welcome2} Você é nosso cliente a quantos meses?'))
cliente3 = int(input(f'{welcome3} Você é nosso cliente a quantos meses?'))
cliente4 = int(input(f'{welcome4} Você é nosso cliente a quantos meses?'))
cliente5 = int(input(f'{welcome5} Você é nosso cliente a quantos meses?'))

valor_produto = 130
desconto_novo = valor_produto * 0.05
desconto_1_a_6meses = valor_produto * 0.10
desconto_7_a_12meses =  valor_produto * 0.012




#Cliente 1
if cliente1 == 0:
    valor_com_desconto = valor_produto - desconto_novo
    print(f'Olá {welcome}, seja bem vindo a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_novo} e só precisará pagar R${valor_com_desconto}')

elif cliente1 >= 1 and cliente1 <= 6:
        
    valor_com_desconto = valor_produto - desconto_1_a_6meses
    print(f'Olá {welcome}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_1_a_6meses} e só precisará pagar R${valor_com_desconto}')

else:
    valor_com_desconto = valor_produto - desconto_7_a_12meses
    print(f'Olá {welcome}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_7_a_12meses} e só precisará pagar R${valor_com_desconto}')

#Cliente 2
if cliente2 == 0:
    valor_com_desconto = valor_produto - desconto_novo
    print(f'Olá {welcome2}, seja bem vindo a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_novo} e só precisará pagar R${valor_com_desconto}')

elif cliente2 >= 1 and cliente2 <= 6:
        
    valor_com_desconto = valor_produto - desconto_1_a_6meses
    print(f'Olá {welcome2}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_1_a_6meses} e só precisará pagar R${valor_com_desconto}')

else:
    valor_com_desconto = valor_produto - desconto_7_a_12meses
    print(f'Olá {welcome2}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_7_a_12meses} e só precisará pagar R${valor_com_desconto}')

#Cliente 3
if cliente3 == 0:
    valor_com_desconto = valor_produto - desconto_novo
    print(f'Olá {welcome3}, seja bem vindo a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_novo} e só precisará pagar R${valor_com_desconto}')

elif cliente3 >= 1 and cliente3 <= 6:
        
    valor_com_desconto = valor_produto - desconto_1_a_6meses
    print(f'Olá {welcome3}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_1_a_6meses} e só precisará pagar R${valor_com_desconto}')

else:
    valor_com_desconto = valor_produto - desconto_7_a_12meses
    print(f'Olá {welcome3}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_7_a_12meses} e só precisará pagar R${valor_com_desconto}')

#Cliente 4
if cliente4 == 0:
    valor_com_desconto = valor_produto - desconto_novo
    print(f'Olá {welcome4}, seja bem vindo a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_novo} e só precisará pagar R${valor_com_desconto}')

elif cliente4 >= 1 and cliente4 <= 6:
        
    valor_com_desconto = valor_produto - desconto_1_a_6meses
    print(f'Olá {welcome4}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_1_a_6meses} e só precisará pagar R${valor_com_desconto}')

else:
    valor_com_desconto = valor_produto - desconto_7_a_12meses
    print(f'Olá {welcome4}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_7_a_12meses} e só precisará pagar R${valor_com_desconto}')

#Cliente 5
if cliente5 == 0:
    valor_com_desconto = valor_produto - desconto_novo
    print(f'Olá {welcome5}, seja bem vindo a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_novo} e só precisará pagar R${valor_com_desconto}')

elif cliente5 >= 1 and cliente5 <= 6:
        
    valor_com_desconto = valor_produto - desconto_1_a_6meses
    print(f'Olá {welcome5}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_1_a_6meses} e só precisará pagar R${valor_com_desconto}')

else:
    valor_com_desconto = valor_produto - desconto_7_a_12meses
    print(f'Olá {welcome5}, seja bem vindo de volta a nossa loja! O produto custa R${valor_produto}, mas como você é novo por aqui terá um desconto de R${desconto_7_a_12meses} e só precisará pagar R${valor_com_desconto}')