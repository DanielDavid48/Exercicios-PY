import time

cont = 0 
n = 0
ask = 'S'
lista_elementos = []
while ask != 'N': 
    n = int(input(f'Insira o {cont}° valor: '))
    cont += 1
    ask = str(input('Quer continurar? [S/N] ')).upper()
    lista_elementos.append(n)
    # media
    qtd_strings = len(lista_elementos)
    media = sum(lista_elementos)
    media_final = media / qtd_strings
    # valor maior 
    valor_maior = max(lista_elementos)
    # valor menor
    valor_menor = min(lista_elementos)

    if ask == 'N':
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(f"""Você \033[33mdigitou\033[m {qtd_strings} números. 
A \033[33mmédia\033[m entre eles é: {media_final:.2f}.
O \033[33mvalor maior\033[m digitado foi {valor_maior} e o \033[33mmenor\033[m foi {valor_menor}.""")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('Programa finalizado!')
time.sleep(2)

    else:
        print('\033[31mOpção inválida!\033[m')
        print('Programa finalizado!')
        time.sleep(2)
