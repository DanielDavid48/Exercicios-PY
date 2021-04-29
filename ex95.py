print('Seja bem vindo')

dados_gerais = []
jogadores = {}
continuar = ''
cont = 0
while continuar == '':
    cont += 1
    print(f'\033[36m                       JOGADOR {cont}                            \033[m')
    jogador = jogadores['jogador'] = input('Informe o nome do jogador: ')
    print(f'\033[32mOk, analisaremos o jogador {jogador}.\033[m')
    partidas = jogadores['partidas'] = int(input('Você quer analisar quantas partidas: '))
    jogadores["Gols"] = []
    for x in range(0, partidas):
        jogo = int(input(f'Quantos gols na \033[33m{x + 1}º partida:\033[m '))
        jogadores["Gols"].append(jogo)
    dados_gerais.append(jogadores.copy())
    [jogadores.pop(key) for key in ['Gols', 'jogador', 'partidas']]
    continuar = input('Para continuar: \033[33mENTER\033[m  |  Para sair: \033[33m0\033[m     ')
    while continuar not in "''0":
        print('\033[31mOpção inválida!\033[m')
        continuar = input('Para continuar: \033[33mENTER\033[m  |  Para sair: \033[33m0\033[m     ')    
n = 'nº'
nome = 'JOGADOR'
qtd_gols = 'QUANTIDADE DE GOLS'
partidas1 = 'PARTIDAS'
gols = 'GOLS'
contador = 0
print('\033[33m====================================================== ANÁLISE GERAL =========================================================\033[m')
print(f'\033[33m{n:<4}  |  {nome:^30}  |  {gols:^30}  |  {qtd_gols:^25}  |  {partidas1:^25}\033[m')
print('='*140)
for dicionario in dados_gerais:
    for keys in dicionario.values():   
        qtd_gols = sum(dicionario["Gols"])
        print(f'{contador:<4}  \033[33m|\033[m  {dicionario["jogador"]:^30}  \033[33m|\033[m  {str(dicionario["Gols"]):^30}  \033[33m|\033[m  {qtd_gols:^25}  \033[33m|\033[m  {dicionario["partidas"]:^20}  ')
        contador += 1
        break
opcao_alone = input("""Quer ver o levantamento pessoal de algum jogador?
\033[33msim | não:\033[m """).lower()[0]
contador_jogos = 0
if opcao_alone == 's':
    while opcao_alone == 's':
        print('\033[33mDICA: O código do jogador está antes do nome dele no levantamento geral!\033[m')
        jogador_levantamento = int(input('Insira o código do jogador: '))
        print(f'Mostrando o levantamento pessoal do jogador {dados_gerais[jogador_levantamento]["jogador"]}')
        for x in dados_gerais[jogador_levantamento]["Gols"]:
            print(f'No jogo \033[33m{contador_jogos + 1}\033[m ele fez \033[33m{x} gols\033[m')
            contador_jogos += 1
        opcao_alone = input("""Quer ver o levantamento pessoal de algum jogador?
\033[33msim | não:\033[m """).lower()[0]

else:
    print()
print('\033[32mOK, foi um prazer tê-lo conosco aqui!\033[m')
print('Programa finalizado!')