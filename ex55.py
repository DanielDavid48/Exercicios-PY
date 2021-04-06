
lista_pesos = []

for x in range(5):
    peso = float(input('Insira o peso: '))
    lista_pesos.append(peso)

menor = min(lista_pesos)
maior = max(lista_pesos)

print(f"""Na lista obtida de pesos, há os seguintes pesos {lista_pesos}
\033[32mO maior peso é {maior}.\033[m
\033[31mO menor peso é {menor}.\033[m""")