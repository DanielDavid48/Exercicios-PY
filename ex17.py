import math

print('Seja bem vindo')

ca = float(input('Insira o cateto adjacente: '))
co = float(input('Insira o cateto oposto: '))

#ca1 = ca ** 2
#co2 = co ** 2
#hipo = ca + co2
#hipo2 = hipo ** (1/2)

#ou pode importar a biblioteca math

h1 = math.hypot(ca, co)

print(f'A hipotenusa do cateto oposto {co} e do cateto adjacente {ca} é {h1:.2f}')