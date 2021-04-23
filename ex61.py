print('Cálcular progressão aritmética <><><><>')

termo = int(input('Insira o 1° termo: '))
razao = int(input('Insira a razão: '))
qtd = int(input('Quantos termos você quer ver: '))

termoo = termo

cont = 1

while cont <= qtd:
    print(termoo)
    termoo += razao
    cont += 1

print('FIM')
    
