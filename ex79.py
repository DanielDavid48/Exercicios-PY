print('Seja bem vindo!')

lista_num = []
continuar = ''
while continuar == '':
    n = int(input('Digite um valor: '))
    if n not in lista_num:
        lista_num.append(n)
        print('\033[32mNúmero adicionado com sucesso.\033[m')
        continuar = input("""Para continuar: aperte \033[33mENTER\033[m
Para sair: Insira \033[33m0\033[m: """)
        while continuar not in "''0":
            continuar = input("""Para continuar: aperte \033[33mENTER\033[m
Para sair: Insira \033[33m0\033[m: """)
            
    elif n in lista_num:
        print('\033[31mEste número já está na lista. Número não adicionado!\033[m')
        continuar = input("""Para continuar: aperte \033[33mENTER\033[m
Para sair: Insira \033[33m0\033[m: """)
        while continuar not in "''0":
            continuar = input("""Para continuar: aperte \033[33mENTER\033[m
Para sair: Insira \033[33m0\033[m: """)
        
print('\033[33m~-~-~-~-~~-~-~~-~-~-~~-~-~-~~-~-~~-~-~~-~-~-~~-~-~-~~-~-~-~~-\033[m')
print(f'Você inseriu os valores \033[32m{sorted(lista_num)}\033[m')
print('\033[33m~-~-~-~-~~-~-~~-~-~-~~-~-~-~~-~-~~-~-~~-~-~-~~-~-~-~~-~-~-~~-\033[m')
print('Programa finalizado.')