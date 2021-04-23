
print('Seja bem vindo!')

while True:
    n = int(input('Calcular tabuada do número: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'A tabuada do número {n} é: ')
    for x in range(1, 11):
        tabuada = n * x
        print(f'{n} x {x} = {tabuada}')
    opcao = input('Aperte \033[33mENTER\033[m para sair ou digite \033[33m0\033[m para calcular outra tabuada: ')

    if opcao == '0':
        while opcao == '0':
            n = int(input('Calcular tabuada do número: '))
            print(f'A tabuada do número {n} é: ')
            for x in range(1, 11):
                tabuada = n * x
                print(f'{n} x {x} = {tabuada}')
            opcao = input('Aperte \033[33mENTER\033[m para sair ou digite \033[33m0\033[m para calcular outra tabuada: ')
        if  opcao == '':
            break

    elif opcao == '':
        break

    else:
        print('\033[31mOpção inválida!\033[m')
        break

print('\033[33mprograma finalizado!\033[m')
