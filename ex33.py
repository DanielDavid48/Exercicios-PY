print('Seja bem vindo!')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

 #verificando o menor valor

menor = n1
if n2<n1 and n2<n3:
    menor = n2

if n3<n1 and n3<n2:
    menor = n3

# descobrindo o maior valor

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f"""analisando os valores {n1}, {n2} e {n3}. 
O maior valor é {maior}.
O menor valor é {menor}.""")