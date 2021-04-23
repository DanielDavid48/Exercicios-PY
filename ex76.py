produtos = ('Bicicleta', 1000, 'Celular', 1200, 'Mini ventilador', 12)

print('\033[36m                LISTA                 \033[m')
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
        
    else:
        print(f'R$ {produtos[pos]:>7.2f}')