# desafio 1: escreva um programa para aprovr o emprestimo bancario para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal sabendo que ela noa pode exceder 30% do salario ou entao o emprestimo sera negado

#from colorama import Fore, Back, Style
#import os

#print('Seja bem vindo ao Banco do POVO!')

#nome = str(input('Me informe seu nome por gentileza: '))
#print(f'Prazer em te conhecer {nome}')

#print(f'{nome}, qual é o valor da casa?')
#valor_casa = float(input('Valor da casa: R$ '))
#print(f'Ok {nome}, então o valor da casa é {valor_casa}.... Anotei aqui.')
#print(f'{nome}, qual é o seu salário atual?')
#salario = float(input('Meu salário atual é: R$ '))
#print('ok, agora uma última informação, em quantos anos quer pagar essa casa?')
#anos = int(input('Digite aqui: '))

# convertendo anos em meses
#anos_meses = anos * 12

# calculando as parcelas
#parcela = valor_casa / anos_meses

# calculando se excede os 30% do salario
#salario1 = 30 * salario
#salario2 = salario1 / 100

#if parcela > salario2:
#    print(f'\033[31m{nome}\033[m, \033[31minfelizmente o valor da parcela mensal excede 30% do seu salário, {os.linesep}por isso, estamos negando seu empréstimo!\033[30m') 
#    print('\033[m-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\033[m')
#    print('\033[31mVeja um resumo sobre o RECUSAMENTO:\033[m') 
#    print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
#    print(f'>>> O seu salário atual é R${salario:.2f} reais.{os.linesep}>>> 30% do seu salário é igual a R${salario2:.2f}.{os.linesep}>>>> O nosso banco, não aceita parcelamentos que excedam 30% do salário.{os.linesep}>>> Você pode tentar aumentar os anos à pagar ou encontrar uma residência com um valor menor.')
#    print('-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')

#elif parcela <= salario2:
#    print(f"""\033[32m{nome}, o seu empréstimo foi aprovado, o valor das 
#parcelas ficará em R${parcela:.2f} reais mensais!\033[m""")

########################################################################################################################

# desafio 2: Escreva um programa que leia dois numeros inteiros e compare-os. Mostrando na tela uma mensagem:
# o primeiro valor e maior; O segundo valor e maior; nao existe valor maior, os dois sao iguais

#print('Seja bem vindo!')

#n1 = int(input('Insira o primeiro valor: '))
#n2 = int(input('Insira o segundo valor: '))

#if n1 > n2:
#    print(f'O número {n1} é maior que {n2}.')

#elif n2 > n1:
#    print(f'O número {n2} é maior que {n1}.')

#else:
#    print(f'O número {n1} e {n2} saõ iguais, portanto não existe valor maior!')

#####################################################################################################################
# desafio 3: Façaum programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# se ele ainda vai se alistar ao serviço militar; se e a hora de se alistar ou se ja passou o tempo do alistamento
# seu programa tambem devera mostrar o tempo que falta ou que passou do prazo

#print('Seja bem vindo ao ALISTEI?')
#nome = str(input('Informe seu nome: '))
#print(f'Prazer em te conhecer {nome}!')
#idade = int(input('Informe sua idade: '))

# verificando
#dia_alistamento = 18 - idade
#atraso = idade - 18

#if idade < 18:
#    print(f'{nome}, \033[32mvocê ainda não completou 18 anos, então deverá se alistar em {dia_alistamento} ano (s)!\033[m')

#elif idade > 18:
#    print(f'{nome}, \033[31mvocê passou do prazo de se alistar, você deveria ter se alistado à {atraso} ano (s) atrás!\033[m')

#elif idade == 18:
#    print(f'{nome}, \033[33mVocê deverá se alistar agora! Acesse o site da junta militar e se aliste!\033[m')

#####################################################################################################################

# desafio 4: crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de
#acordo com a média atingida:

#print('Seja bem vindo à escola Costa Braga!')
#nome_professor = str(input('Primeiro me informe seu nome: '))
#print(f'Ok, que bom vê-lo novamente {nome_professor}!')
#nome_aluno = str(input('Me informe o nome do aluno: '))
#print(f'Ok, achei o aluno {nome_aluno} aqui no sistema!')

# medias
#media1 = float(input('Insira a primeira nota: '))
#media2 = float(input('Insira a segunda nota: '))
#media3 = float(input('Insira a terceira nota: '))
#media4 = float(input('Insira a quarta nota: '))
#media5 = float(input('Insira a quinta nota: '))

# contando a media
#media_all = (media1 + media2 + media3 + media4 + media5)/5

#if media_all < 5.0:
#    print(f'Caro prefossor (a) {nome_professor}, o aluno  {nome_aluno} foi \033[31mreprovado!\033[m')

#elif media_all >= 5.0 and media_all < 6.9:
#    print(f'Caro professor (a), o aluno (a) {nome_aluno} deverá fazer uma \033[33mrecuperação!\033[m')

#elif media_all > 7.0:
#    print(f'Caro professor (a), o aluno (a) {nome_aluno} foi \033[32maprovado!\033[m')

#######################################################################################################################

# desafio 5: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de uma atleta
# e mostre sua categoria de acordo com a idade: ate 9 anos e mirim; ate 14 anos e infantil; ate 19 anos junior;
# ate 20 anos sênior e acima de 20 anos master

#from datetime import date

#print('Seja bem vindo à CONFEDERAÇÃO DE ESPORTES!')
#nome = str(input('Me informe seu nome por gentileza: '))
#print(f'Que prazer em te conhecer {nome}')
#idade = int(input('Me informe somente o ano que você nasceu: '))

#conta_idade = date.today().year - idade

#if conta_idade <= 9:
#    print(f'{nome}, a sua categoria é \033[34mmirim!\033[m')
 
#elif conta_idade > 9 and conta_idade <= 14:
#    print(f'{nome}, a sua categoria é \033[36minfantil\033[m')

#elif conta_idade > 14 and conta_idade <= 19:
#    print(f'{nome}, a sua categoria é \033[33mjúnior\033[m')

#elif conta_idade > 19 and conta_idade <= 20:
#    print(f'{nome}, a sua categoria é \033[32msênior\033[m')

#elif conta_idade > 20:
#    print(f'{nome}, a sua categoria é \033[35mmaster\033[m')

######################################################################################################################

# desafio 6: Refaca o desafio 35 dos triangulos, acresecntando o recurso de mostrar que tipo de triangulo sera formado
# equilatero: todos os lados iguais. isoceles: dois lados iguais e escaleno todos os lados diferentes

#n1 = float(input('Insira a primeria vértice: '))
#n2 = float(input('Insira a segunda vértice: '))
#n3 = float(input('Insira a terceira vértice: '))



#if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
#    if n1 == n2 == n3:
#        print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} podem formar um \033[32mtriângulo equilatero\033[m')
#    elif n1 == n2 or n1 == n3 or n3 == n2:
#        print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} podem formar um \033[32mtriângulo isóceles\033[m')
#    elif n1 != n2 != n3 != n1:
#        print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} podem formar um \033[32mtriângulo escaleno\033[m')

#else:
#    print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} \033[31mnão podem formar uma triângulo!\033[m')

###################################################################################################################33

# desafiol 7: Desenvolva uma logica que leia o peso e a altura de uma pessoa. Calcule seu IMC e mostre seu status,
# de acordo com a tabela abaixo:
# abaixo de 18.5 é abaixo do peso; entre 18.5 e 25 é peso ideal; 25 ate 30 e sobrepeso; 30 ate 40 e obesidade e acima de
# 40 é obesidade mórbida

#print('Seja bem vindo ao SAUDE VITAL')
#nome = str(input('Me informa seu nome: '))
#print(f'\033[32mPrazer em te conhecer\033[m {nome}!')
#peso = float(input('Me informe seu peso: '))
#print(f'\033[32mOk, você pesa\033[m {peso} \033[32mkilos.\033[m')
#altura = float(input('Me informe sua altura: '))

# calculando o immc
#imc1 = altura * altura
#imc = peso / imc1

#if imc < 17:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mEXTREMAMENTE ABAIXO DO PESO IDEAL!\033[m')
#    print(f'{nome}, recomendamos que procure um médico nutricionista \033[31mURGENTE!\033[m')

#elif imc >= 17 and imc < 18.5:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mABAIXO DO PESO IDEAL!\033[m')
#    print(f'{nome}, recomendamos que procure um médico nutricionista \033[31mO MAIS RÁPIDO POSSÍVEL!\033[m')

#elif imc >= 18.5 and imc < 25:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[32mVOCÊ ESTÁ NO PESO IDEAL!\033[m')

#elif imc >= 25 and imc < 30:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[33mACIMA DO PESO IDEAL!\033[m')
#    print(f'{nome}, recomendamos que procure um médico nutricionista \033[31mO MAIS RÁPIDO POSSÍVEL!\033[m')

#elif imc >= 30 and imc < 35:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mCOM OBESIDADE DE GRAU 1!\033[m')
#    print(f'{nome}, recomendamos que procure um médico nutricionista \033[7;31mURGENTE!\033[m')

#elif imc >= 35 and imc < 40:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mCOM OBESIDADE GRAU 2!\033[m')
#    print(f'{nome}, recomendamos que procure um médico nutricionista \033[7;31mURGENTE!\033[m')

#elif imc >= 40:
#    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mCOM OBESIDADE GRAU 3!\033[m')
#    print(f'{nome}, recomendamos que procure um médico nutricionista \033[7;31mURGENTE\033[m')

#else:
#    print(f'{nome}, você não digitu uma opção váida!')

####################################################################################################################

# desafio 8: elabore um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e 
# condição de pagamento: a vista (dinheiro e cheque) e 10% de desconto; a vista no cartao e 5% de desconto
# em ate 2x no cartao e preco normal e 3x ou mais 20% de juros

#print('\033[32mSeja bem vindo à Davids E-commerce\033[m')
#nome = str(input('Me informe seu nome: '))
#print(f'\033[32Prazer em te conhecer {nome}!\033[m')
#valor = int(input('Insira o valor do produto: R$'))
#print("""Formas de pagamento: 
#1 - À vista (dinheiro ou cheque) 
#2 - À vista no cartão
#3 - Em até 2x no cartão
#4 - 3x ou mais no cartão""")
#opcao = int(input('Digite o número da opção aqui: '))

# avista dinheiro e cheque

#a_vista = 10 * valor
#a_vista1 = a_vista / 100
#a_vista2 = valor - a_vista1

# cartao 1x
#cartao = 5 * valor
#cartao1 = cartao / 100
#cartao2 = valor - cartao1

# ate 2x
#ate2vezes = valor

# 3x ou mais
#vezes3oumais = 20 * valor
#vezes3oumais1 = vezes3oumais / 100 
#vezes3oumais2 = vezes3oumais1 + valor

#if opcao == 1:
#    print(f'{nome}, o produto ficará em R${a_vista2} reais.')

#elif opcao == 2:
#    print(f'{nome}, o produto ficará em R${cartao2} reais.')

#elif opcao == 3:
#    print(f'{nome}, o produto ficará em R${ate2vezes} reais.')

#elif opcao == 4:
#    print(f'{nome}, o produto ficará em R${vezes3oumais2} reais.')

#else:
#    print('\033[31mVocê digitou uma opção inválida!\033[m')

##################################################################################################################

# desafio 9: Faca um jogo que o computador jogue jokenpo com voce.
import emoji
from random import choice

print('Seja bem vindo ao JOKENPO"')
print('\033[32mVocê terá 3 opções para jogar: pedra; papel e tesoura.\033[m')
print("""Opções:
pedra 
papel
tesoura""")
opcao = str(input('\033[32mInsira uma opção: \033[m'))

comandos = ['pedra', 'papel', 'tesoura']
sorteio = choice(comandos)

if sorteio == 'pedra':
    if sorteio == opcao:
        print(f'\033[33mAs jogadas foram iguais, tente novamente!\033[m')

    if opcao == 'papel':
        print(f"""Jogada da máquina: {sorteio}
    Sua jogada: {opcao}
    \033[32mPois então você ganhou!\033[m""")

    if opcao == 'tesoura':
        print(f"""Jogada da máquina: {sorteio}
    Sua jogada: {opcao}
    \033[31mPois então você perdeu!\033[m""")

elif sorteio == 'papel':
    if sorteio == opcao:
        print(f'\033[33mAs jogadas foram iguais, tente novamente!\033[m')

    if opcao == 'pedra': 
        print(f"""Jogada da máquina: {sorteio}
    Sua jogada: {opcao}
    \033[31mPois então você perdeu!\033[m""")

    if opcao == 'tesoura':
        print(f"""Jogada da máquina: {sorteio}
    Sua jogada: {opcao}
    \033[32mPois então você ganhou!\033[m""")

elif sorteio == 'tesoura':
    if sorteio == opcao:
        print('\033[33mAs jogadas foram iguais, tente novamente!\033[m')

    if opcao == 'pedra':
        print(f"""Jogada da máquina: {sorteio}
    Sua jogada: {opcao}
    \033[32mPois então você ganhou!\033[m""")

    if opcao == 'papel':
        print(f"""Jogada da máquina: {sorteio}
    Sua jogada: {opcao}
    \033[31mPois então você perdeu!\033[m""")

else:
    print('\033[31mVocê não inseriu uma opção válida!\033[m')
