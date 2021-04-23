print('Seja bem vindo :D')

cont = 0
cont2 = 0 

while True:
    print('\033[33mDICA: Insira 999 para finalizar o programa e ver as métricas!\033[m')
    n = int(input('Insira um valor: '))
    cont += 1
    if n == 999:
        break
    cont2 += n 

print(f'Você digitou {cont - 1} números, e a soma entre eles resulta em {cont2}.')