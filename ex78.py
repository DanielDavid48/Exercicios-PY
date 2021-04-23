numeros = []
numeros2 = []
for x in range(0, 5):
    n = int(input('Insira um valor: '))
    numeros.append(n)
    numeros2.append(n)

# achando o maior numero
maior = max(numeros2)
posicao_maior = numeros2.index(maior)
numeros.remove(maior)

# achando o menor numero
menor = min(numeros2)
posicao_menor = numeros2.index(menor)
numeros.remove(menor)

# imprimindo resultados
print('\033[32m~-~-~-~~-~-~~-~-~-~~-~-~-~-~-~-~-~~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~~-~-~-~-~-\033[m')
print(f'Você digitou os números \033[35m{numeros2}\033[m')
print(f'Dentre eles, o maior número é \033[33m{maior}\033[m, e ele está na \033[33m{posicao_maior + 1}° posição.\033[m')
if maior in numeros: 
    new = numeros.index(maior) 
    print(f'O maior número, também aparece na \033[33m{new + 3}° posição!\033[m')
print(f'Já o menor é \033[33m{menor}\033[m e ele está na \033[33m{posicao_menor + 1}° posição.\033[m')
if menor in numeros: 
    new = numeros.index(menor) 
    print(f'O menor número, também aparece na \033[33m{new + 3}° posição!\033[m')                                                                                       
print('\033[32m~-~-~-~~-~-~~-~-~-~~-~-~-~-~-~-~-~~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~~-~-~-~-~-\033[m')