n1 = float(input('Insira a primeria vértice: '))
n2 = float(input('Insira a segunda vértice: '))
n3 = float(input('Insira a terceira vértice: '))



if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    if n1 == n2 == n3:
        print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} podem formar um \033[32mtriângulo equilatero\033[m')
    elif n1 == n2 or n1 == n3 or n3 == n2:
        print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} podem formar um \033[32mtriângulo isóceles\033[m')
    elif n1 != n2 != n3 != n1:
        print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} podem formar um \033[32mtriângulo escaleno\033[m')

else:
    print(f'As vértices {n1:.2f}, {n2:.2f} e {n3:.2f} \033[31mnão podem formar uma triângulo!\033[m')
