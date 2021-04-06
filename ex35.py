print('Seja bem vindo')

p1 = float(input('Insira o primeiro seguimento: '))
p2 = float(input('Insira o segundo seguimento: '))
p3 = float(input('Insira o terceiro seguimento: '))

# descobrindo se pode formar
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print(f'Os seguimentos {p1}, {p2} e {p3}, podem formar um triângulo.')
else:
    print(f'Os seguimentos {p1}, {p2} e {p3}, não podem formar um triângulo.')