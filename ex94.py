print('\033[32mSeja bem vindo!\033[m')

dados = []
dicionario_pessoas = {}

contador_pessoas_cadastradas = 0
contador_idade_grupo = 0
cont = 0
continuar = ''
contador_mulheres = 0

while continuar == '':
    cont += 1
    # obtenção de dados
    print(f'\033[36m               CADASTRANDO A {cont}º PESSOA              \033[m')
    nome = dicionario_pessoas['Nome'] = input(f'Insira o nome da {cont}º pessoa: ')
    idade = dicionario_pessoas['Idade'] = int(input(f'Insira a idade do (a) {nome}: '))
    sexo = dicionario_pessoas['Sexo'] = input(f'SEXO: m ou masculino | f ou feminino: ').lower()[0]
    # enquanto o sexo nao for m ou f repete o input ate receber m ou f
    while sexo[0] not in "mf":
        print('\033[31mDigite um sexo válido!\033[m')
        sexo = dicionario_pessoas['Sexo'] = input(f'SEXO: m ou masculino | f ou feminino: ').lower()[0]
    # se sexo for igual a f entao eu acumulo mais 1 no contador_mulheres para calcular a qtd de mulheres
    if sexo[0] == 'f':
        contador_mulheres += 1
    # aqui manda o dicionario pra lista e logo reseta o dicionario pro proximo loop
    dados.append(dicionario_pessoas.copy())
    [dicionario_pessoas.pop(key) for key in ['Nome', 'Idade', 'Sexo']]
    # aqui da a opcao de adicionar mais um ou sair do while
    continuar = input('Continuar: \033[33mENTER\033[m  |  Sair: \033[33m0\033[m    ')
    # enquanto o input de continuar nao receber (nada = ENTER) ou 0 repete o input
    while continuar not in "''0":
        print('\033[31mOpção inválida!\033[m')
        continuar = input('Continuar: \033[33mENTER\033[m  |  Sair: \033[33m0\033[m    ')
    # esse contador calcula a idade do grupo
    contador_idade_grupo += idade
    
media_idade = contador_idade_grupo / cont

print('Analisando a lista, verificamos os seguintes:')
print(f"""Foram cadastradas {cont} pessoas.
A média de idade do grupo é de {media_idade:.2f} anos.""")
# se contador_nulheres for maior que 0 significa que ha mulheres na lista, entao imprime os dados respectivos abaixo
if contador_mulheres > 0:
    print(f'\033[35mAs mulheres cadastradas são:\033[m', end= ' ')
    for x in dados:
        for i in x.items():
            if x["Sexo"] == 'f':
                print(f'{x["Nome"]}', end= ', ') 
                break
else:
    print('\033[33mNão foram cadastradas nenhuma mulher!\033[m')
    
# aqui e responsavel por imprimir as pessoas com idade acima da media de idade geral
print(f'\033[33mAs pessoas com idade acima da média do grupo que é {media_idade:.2f} são:\033[m', end= ' ')
for n in dados:
    for n in x.items():
        if x["Idade"] > media_idade:
            print(f'{x["Nome"]}', end= ', ')
            break
        
# pra fins de teste  
print(dados)
print(dicionario_pessoas)