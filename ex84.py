print('Seja bem vindo!')
geral = []
dados = []
contador_pessoas_cadastradas = 0
cont_maior_80 = 0
cont_menor_80 = 0
cont = 1
continuar = ''
while continuar == '':
    print(f'\033[36m            CADASTRANDO O {cont}° USUÁRIO            \033[m')
    cont += 1
    nome = str(input('Insira o nome da pessoa: '))
    peso = int(input(f'Insira o peso da {nome}: '))
    dados.append(nome)
    dados.append(peso)
    geral.append(dados[:])
    dados.clear()
    if peso >= 80:
        cont_maior_80 += 1
    else:
        cont_menor_80 += 1
    contador_pessoas_cadastradas += 1
    continuar = input("""Para continuar: ENTER
Para sair: 0 """)
    while continuar not in "''0":
        continuar = input("""Para continuar: ENTER
Para sair: 0 """)

if cont_maior_80 != 0:
    print('\033[33mAs pessoas com peso maior de 80kg são:\033[m ')
    for p in geral:
        if p[1] >= 80:
            print(f'{p[0]} com {p[1]}KG.')
else:
    print('\033[31mNão houve nenhuma pessoa com mais de 80kg!\033[m')
    
if cont_menor_80 != 0:
    print('\033[33mAs pessoas com menos de 80kg são:\033[m ')
    for i in geral:
        if i[1] < 80:
            print(f'{i[0]} com {i[1]}KG.')
else:
    print('\033[31mNão houve nenhuma pessoa com menos de 80kg!\033[m')
            
print(f'Ao total, foram cadastradas {contador_pessoas_cadastradas} pessoas.')
