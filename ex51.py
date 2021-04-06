print('Vamos calcular a PA')
n1 = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão da PA:  '))
#total = int(input('Insira quantos termos quer ver: '))

dec_termo = n1 + (10 - 1) * razao

for i in range(n1, dec_termo + razao, razao):
   print(i)