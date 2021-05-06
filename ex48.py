
print('\033[32mBem vindo!\033[m')
primeiro_termo = int(input('Insira o comeco do intervalo: '))
segundo_termo = int(input('Insira o final do intervalo: '))

s = 0
cont = 0
for x in range(primeiro_termo, segundo_termo, 2):
    if x % 3 == 0:
        cont = cont + 1
        s += x
print(f'A soma dos {cont} valores solicitados foi {s}')
print('FIM')