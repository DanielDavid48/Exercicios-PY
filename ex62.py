import time

print('Seja bem vindo!')
termo = int(input('Insira o 1° termo: '))
razao = int(input('Insira a razão: '))
qtd = int(input('Insira quantos termos quer ver: '))


cont = 1

while cont <= qtd:
    print(termo)
    termo += razao
    cont += 1

print('------------------------------')
print("""OPÇÕES:
[ 1 ] ver mais termos
[ 2 ] finalizar programa""")

opcao = input('Insira a opção: ')

if opcao == '1':
    mais = int(input('Você quer ver mais quantos termos: '))
    cont1 = 1
    while cont <= mais:
        print(termo)
        termo += razao
        cont1 += 1

elif opcao == '2':
    print('Finalizando programa...')
    print('Programa finalizado!')
    time.sleep(1)

else:
    print('Opcao invalida!')

    print('Programa finalizado!')
    time.sleep(1)
