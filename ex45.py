import emoji
from random import choice

print('Seja bem vindo ao JOKENPO"')
print('\033[32mVocê terá 3 opções para jogar: pedra; papel e tesoura.\033[m')
print("""Opções:
pedra 
papel
tesoura""")
opcao = str(input('\033[32mInsira uma opção: \033[m'))

comandos = ['pedra', 'papel', 'tesoura']
sorteio = choice(comandos)

if sorteio == 'pedra':
    if sorteio == opcao:
        print(f'\033[33mAs jogadas foram iguais, tente novamente!\033[m')

    if opcao == 'papel':
        print(f"""Jogada da máquina: {sorteio}
Sua jogada: {opcao}
\033[32mPois então você ganhou!\033[m""")

    if opcao == 'tesoura':
        print(f"""Jogada da máquina: {sorteio}
Sua jogada: {opcao}
\033[31mPois então você perdeu!\033[m""")

elif sorteio == 'papel':
    if sorteio == opcao:
        print(f'\033[33mAs jogadas foram iguais, tente novamente!\033[m')

    if opcao == 'pedra': 
        print(f"""Jogada da máquina: {sorteio}
Sua jogada: {opcao}
\033[31mPois então você perdeu!\033[m""")

    if opcao == 'tesoura':
        print(f"""Jogada da máquina: {sorteio}
Sua jogada: {opcao}
\033[32mPois então você ganhou!\033[m""")

elif sorteio == 'tesoura':
    if sorteio == opcao:
        print('\033[33mAs jogadas foram iguais, tente novamente!\033[m')

    if opcao == 'pedra':
        print(f"""Jogada da máquina: {sorteio}
Sua jogada: {opcao}
\033[32mPois então você ganhou!\033[m""")

    if opcao == 'papel':
        print(f"""Jogada da máquina: {sorteio}
Sua jogada: {opcao}
\033[31mPois então você perdeu!\033[m""")

else:
    print('\033[31mVocê não inseriu uma opção válida!\033[m')