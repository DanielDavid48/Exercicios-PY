from random import randint
import time

print('\033[33m             BEM VINDO AO ASSISTENTE DE APOSTAS              \033[m')


lista_jogos = []
dados = []

numero_jogos = int(input('Quantos jogos você quer gerar: '))
cont = 0
print(f'\033[33mGerando os {numero_jogos} jogos...\033[m')
time.sleep(1)
for x in range(0, numero_jogos):
    cont += 1
    for s in range(0, 6):
        sorteio = randint(1, 60)
        if sorteio in dados: 
            sorteio1 = randint(1, 60)
            dados.append(sorteio1)
        else:
            dados.append(sorteio)
    lista_jogos.append(dados[:])
    dados.clear()
    print(f'\033[33mJogo {cont}:\033[m {lista_jogos[x]}')
    time.sleep(1)

print(f'\033[32mGeramos ao todo {numero_jogos} jogos. Desejamos boa sorte em sua aposta.\033[m')
print('\033[32m                     SISTEMA FINALIZADO               \033[m')

