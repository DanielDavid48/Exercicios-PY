from random import choice

print('Vamos adivinhar?')
chute = int(input('Chute um número entre 0 e 5: '))

# sorteio
list = [0, 1, 2, 3, 4, 5]
sorteio = choice(list)

if chute == sorteio:
    print(f"""Você acertou em cheio pequeno gafanhoto! 
O número escolhido foi {sorteio}""")

else:
    print(f"""Infelizmente você errou! 
O número escolhido foi {sorteio}""")