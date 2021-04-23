from os import linesep
import time


n = 0
ask = 'S'
lista_elementos = []
termos_inaceitaveis = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
while ask not in termos_inaceitaveis:
    n = int(input(f'Insira um valor: '))
    lista_elementos.append(n)
    # media
    qtd_strings = len(lista_elementos)
    media = sum(lista_elementos)
    media_final = media / qtd_strings
    # valor maior
    valor_maior = max(lista_elementos)
    # valor menor
    valor_menor = min(lista_elementos)
    ask = str(input('Quer continurar? [S/N] ')).upper()
    lista_aceitaveis = ['S', 'N']
    while ask not in lista_aceitaveis:
        ask = str(input('Opção inválida! Quer continurar? [S/N] ')).upper()
        
    

if ask == 'N':
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Você \033[33mdigitou\033[m {qtd_strings} números.{linesep}A \033[33mmédia\033[m entre eles é: {media_final:.2f}.{linesep}O \033[33mvalor maior\033[m digitado foi {valor_maior} e o \033[33mmenor\033[m foi {valor_menor}.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Programa finalizado!')
    time.sleep(2)
        
else:
    print('\033[31mOpção inválida!\033[m')
    print('Programa finalizado!')
    time.sleep(2)
           