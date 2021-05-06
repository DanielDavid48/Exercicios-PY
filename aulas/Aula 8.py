#import math
#num = int(input('Digite um número: '))
#raiz = math.sqrt(num)

#print(f'A raiz de {num} é igual a {raiz}')

######################################################################################3
#import random
#num = random.randint(1, 10)
#print(num)

#########################################################################################

# Desafio 1: crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: digite um numero: 6.127
# o numero 6.127 tem a parte inteira 6

#import math

#n = float(input('Digite um número: '))

#i = math.trunc(n)
#print(i)

###############################################################################################3

# Desafio 2: Faça um programa que leia o comprimento do cateto oposto edo cateto adjacente de um triângulo retângulo
#calule e mostre o comprimento da hipotenusa

#import math

#co = float(input('Insira o tamanho do comprimento do cateto oposto: '))
#ca = float(input('Insira o tamanho do comprimento do cateto adjacente: '))

#hipo = co ** 2 
#hipo2 = ca ** 2
#hipo3 = hipo + hipo2
#hipo4 = hipo3 ** (1/2)

#print(f'A hipotenusa é {hipo4}')

##########################################################################################################################

# Desafio 3: faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

#import math

#angulo = float(input('Insira um ângulo: '))

#angulo1 = math.radians(angulo)

#seno cosseno e tangente

#seno = math.sin(angulo1)
#cosseno = math.cos(angulo1)
#tangente = math.tan(seno + cosseno)

#print(f'O seno do ângulo {angulo} é {seno}')
#print(f'O cosseno do ângulo {angulo} é {cosseno}')
#print(f'A tangente do ângulo {angulo} é {tangente}')

#import os
#from math import sin, cos, tan, radians

#angulo = float(input('Digite o angulo: '))

#print(f'O ângulo{angulo}, possui:{os.linesep}Seno: {sin(radians(angulo)):.2f}{os.linesep}Cosseno: {cos(radians(angulo)):.2f}{os.linesep}Tangente: {tan(radians(angulo)):.2f}')

#########################################################################################################################3Desafio 4: Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.


#from random import choice

#aluno1 = input('Salve salve, qual seu nome meu chegado?')
#aluno2 = input('Salve salve, qual seu nome meu chegado?')
#aluno3 = input('Salve salve, qual seu nome meu chegado?')
#aluno4 = input('Salve salve, qual seu nome meu chegado?')

#lista_alunos = [aluno1, aluno2, aluno3, aluno4]

#aluno_escolhido = choice(lista_alunos)

#print(f'Salve salve meus chegados, o azarado da vez foi o {aluno_escolhido}')


#########################################################################################################################

#Exercicio extra do Mathews Vagal: Crie um programa que irá registrar o nome de 5 clientes de uma loja. Essas pessoas serão selecionadas para um sorteio, quem ganhar o sorteio terá o seu pedido de graça, e um dos perdedores terá que pagar o valor do pedido do ganhador.

#from random import choice

#print('Bem vindo ao sorteio!')
#print('Para comecarmos, registre o nome dos participantes abaixo...')

# participantes

#participante1 = input('Participante 1: ')
#participante2 = input('Participante 2: ')
#participante3 = input('Participante 3: ')
#participante4 = input('Participante 4: ')
#participante5 = input('Participante 5: ')

#lista_participantes = [participante1, participante2, participante3, participante4, participante5]

#sorteio = choice(lista_participantes)

#print(f'O cliente escolhido no sorteio foi {sorteio}')

#Dando uma dica: seria bom tu criar uma lista com o resto não sorteado, dando outra dica use if
#Uma obs.: Não precisa ficar mudando os nomes das variaveis dentro dos ifs e elifs, pq cada um é uma condição diferente e só vai entrar naquela condição se for verdadeira.pode contin

#if sorteio == participante1:
    #lista_participantes_restantes = [participante2, participante3, participante4, participante5]
    #sorteio2 = choice(lista_participantes_restantes)
    #print(f'E o cliente azarado foi {sorteio2}')

#elif sorteio == participante2:
    #lista_participantes_restantes = [participante1, participante3, participante4, participante5]
    #sorteio2 = choice(lista_participantes_restantes)
    #print(f'E o cliente azarado foi {sorteio2}')

#elif sorteio == participante3:
    #lista_participantes_restantes = [participante1, participante2, participante4, participante5]
    #sorteio2 = choice(lista_participantes_restantes)
    #print(f'E o cliente azarado foi {sorteio2}')

#elif sorteio == participante4:
    #lista_participantes_restantes = [participante1, participante2, participante3, participante5]
    #sorteio2 = choice(lista_participantes_restantes)
    #print(f'E o cliente azarado foi {sorteio2}')

#elif sorteio == participante5:
    #lista_participantes_restantes = [participante1, participante2, participante3, participante4]
    #sorteio2 = choice(lista_participantes_restantes)
    #print(f'E o cliente azarado foi {sorteio2}')

#else:
    #print('Nenhum clientes foi sorteado.')
 
###################################################################################################################
# desafio 5: o mesmo professor do desafio 19 quer sortear a ordem de apresentacao de trabalho dos alunos; Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#import random 

#print('Bem vindo professor!')

#aluno1 = input('Insira o nome do aluno 1: ')
#aluno2 = input('Insira o nome do aluno 2: ')
#aluno3 = input('Insira o nome do aluno 3: ')
#aluno4 = input('Insira o nome do aluno 4: ')

#lista = [aluno1, aluno2, aluno3, aluno4]

#random.shuffle(lista)

#print(f'A lista de alunos para apresentação foi sorteada nessa ordem:')
#print(lista)

###############################################################################################################3

# Desafio 6: Faça um prgrama que abra e reproduza um audio de um arquivo mp3

# Importando o PyGame
import pygame
import os

# Inicializando o PyGame
pygame.init()

# Carregando o arquivo MP3 e executando
if os.path.exists('teste.mp3'):
    pygame.mixer.music.load('teste.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo musica.mp3 não está no diretório do script Python')