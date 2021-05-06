from random import randint

lista = []
dicionario = {}
cont = 0
for x in range(0, 4):
    cont += 1
    sorteio = dicionario[f'Jogador {cont}'] = randint(1, 12)
    print(f'\033[33mJogador {cont} jogou:\033[m {dicionario[f"Jogador {cont}"]}')

print('\033[33m==================== RANKING ========================\033[m')
contador = 0
for item in sorted(dicionario, reverse= True, key = dicionario.get):
    contador += 1
    print(f'\033[32m{contador}º lugar\033[m = \033[33m{item}\033[m com o número \033[33m{dicionario[item]}.\033[m')

