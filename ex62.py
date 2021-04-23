import time

print('Seja bem vindo!')
termo = int(input('Insira o 1° termo: '))
razao = int(input('Insira a razão: '))
qtd = int(input('Insira quantos termos quer ver: '))

termo1 = termo
voltar = ''
cont = 1

while cont <= qtd:
    termo1 += razao
    cont += 1
    print(termo1)

while voltar == '':
    print('\033[33m------------------------------\033[m')
    print("""OPÇÕES:
    \033[33m[ 1 ]\033[m ver mais termos
    \033[33m[ 2 ]\033[m finalizar programa""")

    opcao = input('Insira a opção: ')

    if opcao == '1':
        mais = int(input('Você quer ver mais quantos termos: '))
        total = qtd + mais
        #qtd_termos = qtd
        cont1 = cont
        while cont1 <= total:
            termo1 += razao
            cont1 += 1
            print(termo1)
        voltar = input('Aperte ENTER para voltar ao menu! ')

    elif opcao == '2':
        conta = total
        print(f'\033[33mFinalizando programa com {total} termos mostrados...\033[m')
        time.sleep(1)
        break

    else:    
        print('\033[31mOpcao invalida!\033[m')
    

print('Programa finalizado!')    
time.sleep(1)
