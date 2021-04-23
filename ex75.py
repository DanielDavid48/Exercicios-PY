tupla_valores = (int(input('Digite um número: ')), int(input('Digite o 2° número: ')), 
                 int(input('Digite o 3° número: ')), int(input('Digite o ultimo número: ')))


pares = []
for numero in tupla_valores:
    if numero % 2 == 0:
        pares.append(numero)
        
if 9 in tupla_valores:
    qtd_9_tupla = tupla_valores.count(9) 
    print(f'O número 9 apareceu {qtd_9_tupla} vezes')
    
else:
    print('Não foram digitados nenhum número 9!')
    
if 3 in tupla_valores:
    posicao_3_tupla = tupla_valores.index(3)
    print(f'O número 3 foi digitado na {posicao_3_tupla + 1}° posição!')
else:
    print('Não foi digitado nenhum valor 3!')
    
leitor = len(pares)
if leitor > 0:
    print(f'Os números pares digitados foram: {pares}')

else:
    print('Não foram digitados nenhum número par!')