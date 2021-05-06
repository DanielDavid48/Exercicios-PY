# Desafio 1: Escrev e peça para 
# a um programa que faca o computador pensar em um numero inteiro entre 0 e 5 e peca para o usuario
#tentar descobrir qual foi o numero escolhido pelo computador o prorama devera indicar se ela acertou ou errou.

#from random import choice

#print('Olá, vamos adivinhar?')

#nome_usuario = str(input('Insira seu nome primeiro: '))
#print(f'Prazer em te conhecer {nome_usuario}.')
#tentativa = int(input('Tente advinhar o número entre 0 e 5: '))

#list = [0, 1, 2, 3, 4, 5]
#escolhendo = choice(list)

#if tentativa == escolhendo:
#    print(f'Parabéns {nome_usuario}, você acertou em cheio o número. ')

#else:
#    print(f'{nome_usuario}, infelizmente você errou. O número escolhido era {escolhendo}.')

########################################################################################################################

# desafio 2: Escreva um programa que leia a velocidade de um carro e se ele ultrapassar 80km/h mostre uma mensagem
# dizendo que ele foi multado.
# a multa vai custar R$7 por cada km acima do limite


#print('Seja bem vindo, vamos calcular sua multa')
#print('Qual é o seu nome?')
#nome = str(input('Informe seu nome: '))
#print(f'Prazer {nome}.')
#print('Qual era a rodovia?')
#rodovia = str(input('A rodovia era: '))
#print(f'Qual é a cidade que se encontra a rodovia {rodovia}?')
#cidade = str(input('A cidade é: '))
#print(f'Qual é o estado que se encontra a rodovia {rodovia}?')
#estado = str(input('O estado é: '))
#print('Qual era a sua velocidade?')
#velocidade = int(input('Minha velocidade era: '))

# calculando a multa

#calculo = velocidade - 80
#calculo2 = calculo * 7

#if velocidade >= 80:
#    print(f"""Prazer {nome}, Você passou à {velocidade}km/h sendo que o limite de velocidade é de 80Km/h.
3    #>>> Visão geral da sua infração:
#    -------------------------------------LOCAL------------------------------------------
#    >>> Rodovia: {rodovia}
#    >>> Cidade: {cidade}
#    >>> Estado: {estado}
#    ------------------------------- LIMITE ULTRAPASSADO----------------------------------
#    >>> Limite da rodovia: 80Km/h
#    >>> Você passou à {velocidade}km/h
#    --------------------------------------MULTA--------------------------------------------
#    É cobrado R$7 por km acima do limite, portanto você passou {calculo}km/h acima do limite, por isso
#    sua multa será no valor de R${calculo2}""")
#else:
#    print(f"""A velocidade da rodovia {rodovia} é de 80Km/h e 
#    você passou à {velocidade}Km/h, por isso não foi multado""")

############################################################################################################3
# deafio 3: crie um programa que leia um numero inteiro e mostre se ele é par ou impar

#print('Par ou impar?')

#n = int(input('Insira um numero para verificarmos: '))

# descobrindo se e impar ou par

#par = n % 2  

#if par == 0:
#    print(f'O número {n} é par.')

#else:
#    print(f'O número {n} é impar')

##############################################################################################################3

#desafio 4: Desenvolva um programa que pergunte a distancia de uma viagem em km, Calcule o preço da passagem
# cobrando R$0,50 por km para viagens até 200km e R$0.45 para viagens mais longas

#print('Seja bem vindo à Buser.')

#nome_usuario = str(input('Informe seu nome por gentileza: '))
#print(f'Prazer em te conhecer {nome_usuario}')

#print(f'Caro {nome_usuario}, qual é a distância da viagem em KM?')
#distancia = float(input('Distância da viagem: '))

# preco viagem ate 200km
#viagem = distancia * 0.50

# preco viagem mais de 200km
#viagem2 = distancia * 0.45

#if distancia <= 200:
#    print(f'{nome_usuario}, sua viagem custará R${viagem} reais.')

#else:
#    print(f'{nome_usuario}, sua viagem custará R${viagem2} reais.')

#####################################################################################################################33
# desafio 5: Faca um programa que leia um ano e mostre se ele e bissexto.

#print('Esse ano é BISSEXTO?')
#ano = int(input('Insira o ano aqui: '))

#if (ano%4==0 and ano%100!=0) or (ano%400==0):
#    print(f'O ano {ano} é bissexto')
#else:
#    print(f'O ano {ano} não é bissexto')

#################################################################################################################33
# desafio 6: faca um programa que leia 3 numeros e mostre qual é o maior e qual e o menor

#print('Seja bem vindo ao Numerarizei')
#n1 = int(input('Insira o 1° número: '))
#n2 = int(input('Insira o 2° número: '))
#n3 = int(input('Insira o 3° número: '))

# verificando o menor valor
#menor = n1
#if n2<n1 and n2<n3:
#    menor = n2

#if n3<n1 and n3<n2:
 #   menor = n3

# descobrindo o maior valor
#maior = n1
#if n2>n1 and n2>n3:
#    maior = n2
#if n3>n1 and n3>n2:
#    maior = n3

#print(f"""analisando os valores {n1}, {n2} e {n3}. 
#O maior valor é {maior}.
#O menor valor é {menor}.""")

####################################################################################################################

# desafio 7: escreva um programa que pergunte o salario de um funcionario e calcula o valor do seu aumento
# para salarios superiores à R$1.250 calcule um aumento de 10¨%
# e para salarios inferiores ou iguais o aumento e de 15%

#print('Seja bem vindo ao RH')
#nome_usuario = str(input('Insira o nome do funcionário: '))
#print(f'Que bom, verifiquei aqui o empregado {nome_usuario}, vamos lá!')
#salario = float(input(f'Insira o valor do salário atual sem "." ou "," do funcionário {nome_usuario}: '))

# contando o aumento 10%

#if salario > 1.251:
#    aumento10 = 10 * salario
#    aumento10_1 = aumento10 / 100
#    aumento10_2 = aumento10_1 + salario
#    print(f"""O funcionário {nome_usuario} recebe atualmente R${salario} reais 
#e com o aumento de 10% receberá R${aumento10_2} reais""")

#elif salario <= 1.250:
#    aumento15 = 15 * salario
#    aumento15_1 = aumento15 / 100
#    aumento15_2 = aumento15_1 + salario
#    print(f"""O funcionário {nome_usuario} recebe atualmente R${salario} reais 
#e com o aumento de 15% receberá R${aumento15_2} reais""")

#else:
#    print('Parece que houve um erro, comece novamente!')

##############################################################################################################3

# desafio 8: Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao
# formar um triangulo

print('Seja bem vindo')

p1 = float(input('Insira o primeiro seguimento: '))
p2 = float(input('Insira o segundo seguimento: '))
p3 = float(input('Insira o terceiro seguimento: '))

# descobrindo se pode formar
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print(f'Os seguimentos {p1}, {p2} e {p3}, podem formar um triângulo.')
else:
    print(f'Os seguimentos {p1}, {p2} e {p3}, não podem formar um triângulo.')