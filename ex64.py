print('Seja bem vindo!')
cont = 0
cont2 = 0 
n = 0
while n < 999:
    print('\033[33mDICA: insira 999 pra finalizar o programa :D\033[m')
    n = int(input(f'Insira o {cont + 1}° número: '))
    cont += 1
    cont2 += n 
qtd = cont - 1
qtd_final = cont2 - 999
print(f'Você inseriu {qtd} números e a soma entre todos os números resulta em {qtd_final}')