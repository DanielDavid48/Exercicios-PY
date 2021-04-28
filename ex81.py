print('Seja bem vindo!')

continuar = ''
contador_num = 0
lista = []
lista1 = []
contador2 = 0
while continuar == '':
    contador_num += 1
    n = int(input(f'Digite o valor {contador_num}º valor: '))
    lista.append(n)
    lista1.append(n)
    continuar = input("""Para continuar: \033[33mENTER\033[m
Para sair: \033[33m0\033[m: """)
    
    
lista.sort(reverse=True)

print('\033[35m~-~-~~~-~-~-~~-~-~~-~~-~-~-~~-~~-~-~-~~-~-~~-~-~-~~-\033[m')
print(f'Você digitou os valores {lista1}. Essa lista em ordenação descresecente fica: {lista} ')
print(f'Você digitou ao total {contador_num} números.')
if 5 in lista:
    print(f'Você digitou também o número 5, e ele está na posição {lista.index(5) + 1}.')
else:
    print('Você não digitou o número 5!')
print('\033[35m~-~-~~~-~-~-~~-~-~~-~~-~-~-~~-~~-~-~-~~-~-~~-~-~-~~-\033[m')