print('\033[32mVamos mostrar os números pares!\033[m')

for x in range(1, 50):
    if x % 2 == 0:
        print(x)

print('\033[32mProcesso finalizado!\033[m')