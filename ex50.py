lista = []

for x in range(0, 7):
    n = int(input('Insira um valor: '))
    if n % 2 == 0:
       lista.append(n)
soma = 0
for i in range(len(lista)):
    soma += lista[i]

print('')
print(f'A soma dos valores é {soma}')