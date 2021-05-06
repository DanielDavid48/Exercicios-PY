
def ficha():
    global jogador, gols
    if jogador == '':
        jogador = '<desconhecido>'
    if gols == '' or gols.isalpha():
        gols = 0
    if gols >= 0:
        gols = int(gols)

    print(f'O jogador {jogador} fez {gols} gols (s) no campeonato.')

def line():
    print('\033[33m=\033[m'* 70)

jogador = input('Informe o nome do jogador: ')
gols = input('Informe a quantidade de gols: ')

line()
ficha()
line()