# aula 6
# existem 4 tipos para se calcular: int para numeros inteiros; float para numeros flutuantes "."; 
# Bool para números verdadeiros "True" e falso "False"; 
# str nao e para calcular, apenas se eu quiser juntar os numeros.

#float

#n1 = float(input('insira um numero:'))
#n2 = float(input('insira mais um numero:'))
#soma = n1 + n2
#print(f'A soma entre {n1} e {n2} é igual à: {soma}')

#int

#n1 = int(input('insira um numero:'))
#n2 = int(input('insira mais um numero:'))
#s = n1 + n2
#print(f'A soma entre {n1} e {n2} é igual à: {soma}')

# Desafio 1: Crie um programa que leia dois numeros que mostre a soma entre eles.

#numero1 = int(input('insira um numero:'))
#numero2 = int(input('insira outro um numero:'))
#soma = numero1 + numero2
#print(f'A soma entre {numero1} e {numero2} é igual à: {soma}')

# Desafio 2: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# E todas as informações possiveis sobre ela.

from typing import Type

texto1 = input('Digite algo:')

tipo = texto1.isnumeric()

if tipo == True:
    print(f'{texto1} é numérico? {tipo}')
    print(f'Qual o tipo do {texto1}? ',type(tipo))
    
else:
    print('Você digitou um valor falso')