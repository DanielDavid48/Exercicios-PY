
lista_pesos = []

for x in range(1, 6):
    peso = float(input(f'Insira o peso da {x}° pessoa: '))
    lista_pesos.append(peso)

menor = min(lista_pesos)
maior = max(lista_pesos)

print(f"""Na lista obtida de pesos, há os seguintes pesos {lista_pesos}
\033[32mO maior peso é {maior}Kg.\033[m
\033[31mO menor peso é {menor}Kg.\033[m""")