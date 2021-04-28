print('Seja bem vindo!')

lista_num = [
             [[], [], []],
             [[], [], []],
             [[], [], []]
            ]
soma_pares = 0
for i in range(0, 3):
    for x in range(0, 3):
        lista_num[i][x] = int(input(f'Digite um valor: '))
        if lista_num[i][x] % 2 == 0:
            soma_pares += lista_num[i][x]

for i in range(0, 3):
    for x in range(0, 3):
        print(f'[{lista_num[i][x]:^4}]', end='')
    print()
    
maior_segunda_coluna = max(lista_num[1])
soma_terceira_coluna = lista_num[0][2] + lista_num[1][2] + lista_num[2][2]
print('====================================================')
if soma_pares > 0:
    print(f'A soma dos \033[33mvalores pares\033[m é \033[33m{soma_pares}\033[m.')
else:
    print('\033[31mNão foram digitados nenhum número par!\033[m')
print(f'A soma dos valores da \033[33mterceira coluna\033[m é \033[33m{soma_terceira_coluna}\033[m.')
print(f'O maior valor da \033[33msegunda coluna\033[m é o número \033[33m{maior_segunda_coluna}\033[m.')
