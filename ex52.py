n = int(input("Digite um número: "))
cont = 0

for x in range(1, n + 1):
    if n % x == 0:
        cont += 1

if cont == 2:
    print("O número é primo")
else:
    print("O número não é primo")