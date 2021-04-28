lista_geral = []
lista_par =[]
lista_impar = []

continuar = ''
contador_num = 0
while continuar == '':
    contador_num += 1
    n = int(input(f'Digite o {contador_num}º valor: '))
    lista_geral.append(n)
    if n % 2 == 0:
        lista_par.append(n)
        
    else:
        lista_impar.append(n)
    continuar = input("""Para continuar: ENTER
Para sair: 0 """)
    
print(f"""Analisando os números que você digitou.
A lista geral com eles ficou assim: {lista_geral}""")
if len(lista_par) == 0:
    print('Você não digitou nenhum número par!')
else:
    print(f'A lista somente com os números pares ficou assim: {lista_par}.')
    
if len(lista_impar) == 0:
    print('Você não digitou nenhum número impar!')
else:
    print(f'A lista somente com números impares ficou assim: {lista_impar}.')