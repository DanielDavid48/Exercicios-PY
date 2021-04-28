print('Seja bem vindo!')
# listas
lista_num = [[], [], []]

# quantidade de par e impar dentro da lista
cont_qtd_par = 0
cont_qtd_impar = 0
# obtencao de dados
for i in range(0, 7):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        lista_num[0].append(n)
        cont_qtd_par += 1
        
    else:
        lista_num[1].append(n)
        cont_qtd_impar += 1
        
    lista_num[2].append(n)
        
# inserindo os dados na lista       
lista_par = sorted(lista_num[0])
lista_impar = sorted(lista_num[1])
# aplicaca de condicoes 
print(f'\033[33mVocê digitou os números:\033[m {lista_num[2]}.')
if cont_qtd_par > 0:
    print(f'\033[32mOs números pares desta lista são:\033[m {lista_par}')
else:
    print('\033[31mNão foi digitado nenhum número par!\033[m')
    
if cont_qtd_impar > 0:
    print(f'\033[32mOs números impares desta lista são:\033[m {lista_impar}')
else:
    print('\033[31mNão foi digitado nenhum número impar!\033[m')
    
