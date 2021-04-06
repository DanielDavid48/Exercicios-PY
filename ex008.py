print('Converta metros para centímetros ou milimetros')


opcao = input('Coloque mm pra milimetros e cm para centimetros:')
n1 = float(input('Insira um valor em metros:'))

conta1 = n1 / 0.010000
conta2 = n1 / 0.0010000


if opcao == 'cm':    
    print(f'{n1} metros convertido em centímetros é {conta1} centímetros')

if opcao == 'mm':
    print(f'{n1} metros convertido em milimetros é {conta2} milimetros')