lista = []

for x in range(1, 7):
    n = int(input(f'Insira o {x}° valor: '))
    if n % 2 == 0:
       lista.append(n)
soma = 0
for i in range(len(lista)):
    soma += lista[i]

print('')
print(f'A soma dos valores é {soma}')