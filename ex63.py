from os import linesep

show_termos = int(input('Insira a quantidade termos a ser mostrada na tela: '))#Coleta a quantidade de termos


termo1 = 0#Primeiro termo inicia-se em 0
termo2 = 1#Segundo termo inicia-se em 1

print(f'{termo1} ==> {termo2}', end='')

contador = 3#contador igual a 3, pois já é de conhecimento do usuário termo1 e termo 2, falta você mostrar o usuário o termo3...

while contador <= show_termos:#Repete-se enquanto o contador for menor que o numero de termos a ser mostrado na tela
    termo3 = termo1 + termo2 #Terceiro termo é a soma do 1 e segundo termo
    print(f'==> {termo3} ', end='')#Mostra na tela o termo3(entenda que como você está numa estrutura de looop t3 vai ser termo(n), ou seja, ele vai assumir as posições de acordo com a quantidade inserida em show_termos)
    termo1 = termo2#Desloca o ponteiro do vetor atribuindo termo1 a termo 2
    termo2 = termo3#Desloca o ponteiro do vetor atribuindo termo21 a termo 3
    contador += 1 #contador recebe contador + 1, fazendo a contagem de termos.

print(f'{linesep}Todos os termos foram mostrados na tela!')#mostra na tela a mensagem que representa a finalização da sequência