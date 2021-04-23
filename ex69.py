import time

# dados masculinos
nome_users_mas = []
idade_mas = []

# dados femininos
nome_users_fem = []
idade_fem = []

# lista geral
geral = []

continuar = ''

cont = 0

# coleta de dados
while continuar == '':
    print(f'\033[36m              CADASTRO DE USUÁRIO DE N°{cont + 1}            \033[m')
    nome = input('Insira o nome do usuário: ')
    idade = int(input(f'insira a idade do {nome}: '))
    sexo = input(f'Insira o sexo do {nome} [f/m]: ').lower()
    if sexo not in 'fm':
        print('\033[31mVOcê digitou uma opção inválida!\033[m')
        while sexo[0] not in 'fm':
            print('\033[33mDICA: escreva feminino ou masculino, ou também é só colocar f ou m!\033[m')
            sexo = input(f'Insira um sexo válido [f/m]: ').lower()
    continuar = input('Se deseja continuar aperte ENTER, senão insira 0: ')
    cont += 1
    if sexo[0] == 'm':
        nome_users_mas.append(nome)
        idade_mas.append(idade)
        geral.append(idade)
        
    elif sexo[0] == 'f':
        nome_users_fem.append(nome)
        idade_fem.append(idade)
        geral.append(idade)
        
    else:
        print('ERRO')
        break
    
# filtragem de dados: quantidade de homens cadastrados
lendo_qtd_homens = len(nome_users_mas)

# filtragem de dados: quantidade de mulheres com menos de 20 anos
filtrando_menos_20 = list(filter(lambda x: x < 20, idade_fem))
lendo_menos20 = len(filtrando_menos_20)

# filtragem de dados: pessoas com mais de 18 anos
filtrando_mais_18_geral = list(filter(lambda x: x > 18, geral))
lendo_mais18_geral = len(filtrando_mais_18_geral)

print('\033[33mAnalisando dados...\033[m')
time.sleep(1)
print('A análise de dados foi concluida. Veja o resultado:')
print(f"""Nessa lista há {lendo_qtd_homens} homens nessa lista.
\033[32m~-~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~-~-~~-~-~-~-~-~~-~-~-~-~-~-~~-\033[m
Nessa lista há {lendo_menos20} mulheres com menos de 20 anos.
\033[32m~-~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~-~-~~-~-~-~-~-~~-~-~-~-~-~-~~-\033[m
Nessa lista há {lendo_mais18_geral} pessoas com mais de 18 anos.
\033[32m~-~-~-~-~-~-~-~~-~-~-~-~~-~-~-~-~-~-~-~~-~-~-~-~-~~-~-~-~-~-~-~~-\033[m""")

print('Programa finalizado!')
time.sleep(2)