from random import choice
import time

# bem vindo
print('Seja bem vindo ao \033[36mgameBOX\033[m')

# apresentacao jogador
nome_user = str(input('Insira seu nome pequeno gafanhoto: '))
print(f'Bem vindo {nome_user}, você jogará contra a máquina!')
print('\033[36mO game está começando...\033[m')
time.sleep(2)

# lista pra escolha
lista_numeros_choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# escolha da maquina processo
escolha_maquina = choice(lista_numeros_choice)
escolha_maquina_int = int(escolha_maquina)

# input pro usuario escolher um numero
escolha_user = int(input('Insira um número: '))
# input pro usuario escolher par ou impar
escolha_par_impar1 = str(input('PAR (P) = IMPAR (i): ')).lower()

# validacao de par ou impar. Se o resto for 0 é par e mais que 0, ou seja 1 é impar
conta = escolha_maquina_int + escolha_user
conta2 = conta % 2 

# contador para contabilizacao de acertos
cont = 0

# aqui comeca a validacao inicial de dados
if escolha_par_impar1 == 'p' and conta2 == 0:
    print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
    print('\033[32mVocê ganhou!\033[m')
    cont += 1
    while True:
        # escolha da maquina processo
        escolha_maquina = choice(lista_numeros_choice)
        escolha_maquina_int = int(escolha_maquina)
        # input pro usuario escolher um numero
        escolha_user = int(input('Insira um número: '))
        # input pro usuario escolher par ou impar
        escolha_par_impar1 = str(input('PAR (P) = IMPAR (i): ')).lower()
        # validacao de par ou impar. Se o resto for 0 é par e mais que 0, ou seja 1 é impar
        conta = escolha_maquina_int + escolha_user
        conta2 = conta % 2 
        # validacao de ganhou ou perdeu
        if escolha_par_impar1 == 'p' and conta2 == 0:
            print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
            print(f'\033[32mVocê ganhou!\033[m')
            cont += 1
            
        elif escolha_par_impar1 == 'i' and conta2 == 1:
            print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
            print('\033[32mVocê ganhou!\033[m')
            cont += 1
            
        else:
            print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
            print(f'\033[31mA maquina ganhou após você vencê-la {cont} vezes!\033[m')
            break
                
elif escolha_par_impar1 == 'i' and conta2 == 1:
    print('\033[32mVocê ganhou\033[m')
    cont +=1
    while True:
        # escolha da maquina processo
        escolha_maquina = choice(lista_numeros_choice)
        escolha_maquina_int = int(escolha_maquina)
        # input pro usuario escolher um numero
        escolha_user = int(input('Insira um número: '))
        # input pro usuario escolher par ou impar
        escolha_par_impar1 = str(input('PAR (P) = IMPAR (i): ')).lower()
        # validacao de par ou impar. Se o resto for 0 é par e mais que 0, ou seja 1 é impar
        conta = escolha_maquina_int + escolha_user
        conta2 = conta % 2 
        # validacao de ganhou ou perdeu
        if escolha_par_impar1 == 'i' and conta2 == 1:
            print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
            print('\033[32mVocê ganhou!\033[m')
            cont += 1
        
        elif escolha_par_impar1 == 'p' and conta2 == 0:
            print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
            print('\033[32mVocê ganhou!\033[m')
            cont += 1
            
        else:
            print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
            print(f'\033[31mA maquina ganhou após você vencê-la {cont} vezes!\033[m')
            break
        
else:
    print(f'Você jogou {escolha_user} e máquina jogou {escolha_maquina_int}.')
    print('\033[31mA maquina ganhou!\033[m')
print('\033[33mPrograma finalizado!\033[m')
time.sleep(2)

