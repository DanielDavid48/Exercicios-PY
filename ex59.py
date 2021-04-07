print('Seja bem vindo!')

n1 = float(input('Insira o primeiro numero: '))
n2 = float(input('Insira o segundo numero: '))

print("""Opções: 
[ 1 ] somar
[ 2 ] multiplicar 
[ 3 ] dividir 
[ 4 ] novos numeros
[ 5 ] sair do programa""")

opcoes = input('Insira a opcção escolhida: ')

while opcoes:
    if opcoes == '1':
        somando = n1 + n2
        print(f'A soma resulta em {somando}.')
        break

    if opcoes == '2':
        multiplicando = n1 * n2
        print(f'A multiplicação resulta em {multiplicando}.')
        break

    if opcoes == '3':
        dividindo = n1 / n2
        print(f'A divisão resulta em {dividindo}.')
        break

    continue
print('programa finalizado!')