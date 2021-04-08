
print('Seja bem vindo!')

print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 

voltar = ''

while voltar == '':
    opcoes = input('Insira a opcção escolhida: ')

    if opcoes == '1':
        nsoma = float(input('Insira um número: '))
        nsoma1 = float(input('Insira o outro número: '))
        somando = nsoma + nsoma1
        print(f'A soma resulta em {somando}.')
        voltar = input('Aperte enter para selecionar uma opção!')
        print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 


    if opcoes == '2':
        nmulti = float(input('Insira um número: '))
        nmulti1 = float(input('Insira o outro número: '))
        multiplicando = nmulti * nmulti1
        print(f'A multiplicação resulta em {multiplicando}.')
        voltar = input('Aperte enter para selecionar uma opção!')
        print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 

    if opcoes == '3':
        ndividi = float(input('Insira um número: '))
        ndividi1 = float(input('Insira o outro número: '))
        dividindo = ndividi / ndividi1
        print(f'A divisão resulta em {dividindo}.')
        voltar = input('Aperte enter para selecionar uma opção!')
        print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 

    if opcoes == '4':
        print('\033[33mSaindo do programa...\033[m')
        break
print('programa finalizado!')