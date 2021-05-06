n = int(input("Digite um número: "))
cont = 0

for x in range(1, n + 1):
    if n % x == 0:
        cont += 1

if cont == 2:
    print(f"O número {n} é primo")
else:
    print(f"O número {n} não é primo, ele é divisivel {cont} vezes.")