import time

print('-------------------------CALCULADORA----------------------------------')

print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 

voltar = ''

while voltar == '':
    opcoes = input('Insira a opção escolhida: ')

    if opcoes == '1':
        nsoma = float(input('Insira um número: '))
        nsoma1 = float(input('Insira o outro número: '))
        somando = nsoma + nsoma1
        print(f'{nsoma:.2f} + {nsoma1:.2f} é igual à: {somando:.2f}')
        voltar = input('Aperte ENTER para retornar ao menu!')
        print('\033[33m------------------------------\033[m')
        print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 


    if opcoes == '2':
        nmulti = float(input('Insira um número: '))
        nmulti1 = float(input('Insira o outro número: '))
        multiplicando = nmulti * nmulti1
        print(f'{nmulti:.2f} x {nmulti1:.2f} é igual à: {multiplicando:.2f}')
        voltar = input('Aperte ENTER para retornar ao menu!')
        print('\033[33m------------------------------\033[m')
        print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 

    if opcoes == '3':
        ndividi = float(input('Insira um número: '))
        ndividi1 = float(input('Insira o outro número: '))
        dividindo = ndividi / ndividi1
        print(f'{ndividi:.2f} dividido por {ndividi1:.2f} é igual à: {dividindo:.2f}')
        voltar = input('Aperte ENTER para retornar ao menu!')
        print('\033[33m------------------------------\033[m')
        print("""Opções: 
\033[33m[ 1 ]\033[m somar
\033[33m[ 2 ]\033[m multiplicar 
\033[33m[ 3 ]\033[m dividir 
\033[33m[ 4 ]\033[m sair do programa""") 

    if opcoes == '4':
        print('\033[33mSaindo do programa...\033[m')
        break

time.sleep(1)       
print('programa finalizado!')
