import math 

print('Seja bem vindo')

angulo = float(input('Insira o ângulo: '))

rad = math.radians(angulo)

seno = math.sin(rad)
cos = math.cos(rad)
tang = math.tan(rad)

print(f'O seno de {angulo} é {seno:.2f}')
print(f'O cosseno de {angulo} é {cos:.2f}')
print(f'A tangente de {angulo} é {tang:.2f}')

