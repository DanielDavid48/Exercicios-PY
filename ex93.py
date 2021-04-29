print('Bem vindo ao sistema de rendimento de jogadores! ')

dicionario = {}

nome_jogador = dicionario['Nome'] = input('Insira o nome do jogador (a): ')
print(f'Que legal, ok! Então analisaremos o jogador (a) {nome_jogador}.')
qtd_partidas = dicionario['Partidas'] = int(input(f'Digite a quantidade de partidas que você quer analisar: '))
lista_temp = []
qtd_gols = 0
for x in range(0, qtd_partidas):
    gols = int(input(f'Insira a quantidade de gols na {x + 1}º partida: '))
    lista_temp.append(gols)
    dicionario['Gols'] = lista_temp
    qtd_gols += gols

print(f'\033[33mAnalisando os jogos do jogador (a)\033[m {nome_jogador}:')
print(f'Ele fez ao total \033[32m{qtd_gols} gols\033[m em \033[33m{qtd_partidas} partidas.\033[m')
print(f'Ao total foram {qtd_partidas} partidas jogadas.')
print('\033[36m=========================== ANÁLISE GERAL ==================================\033[m')
for i in range(0, qtd_partidas):
    print(f'Na \033[32mpartida {i + 1}\033[m ele fez \033[33m{dicionario["Gols"][i]} gols.\033[m')