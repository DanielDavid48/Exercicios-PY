num = int(input('Digite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal""")

opcao = int(input('Digite a opção: '))

binar = bin(num)
octa = oct(num)
hexa = hex(num)

if opcao  == 1:
    print(f'{num} convertido para binério é {binar:2}.')

elif opcao == 2:
    print(f'{num} convertido para octal é {octa:2}.')

elif opcao == 3:
    print(f'{num} convertido para hexadecimal é {hexa:2}.')

else:
    print('Opção inválida!')