print('Seja bem vindo')
nomeprofessor = input('Para começarmos me infome seu nome: ')
print(f'Que prazer tê-la (o) por aqui querido (a) {nomeprofessor}!')

lista = []
dicionario = {}

total_alunos = int(input(f'Caro (a) {nomeprofessor} quer analisar quantos alunos: '))
cont = 0
contador_nmr_aprovados = 0
contador_nmr_reprovados = 0

for aluno in range(0, total_alunos):
    cont += 1
    print(f'\033[36m                     {cont}º ALUNO                        \033[m')
    nome = dicionario['Nome'] = input(f'Insira o nome do {cont}º aluno: ')
    media = dicionario['Média'] = float(input(f'Insira a média do aluno {nome}: '))
    lista.append(dicionario.copy())
    if media >= 5:
        contador_nmr_aprovados += 1
    
    else:
        contador_nmr_reprovados += 1
    
print('\033[36mAnalisando os alunos, geramos o relatório: \033[m')
print('~-~'*40)
contador_aprovados = 0
contador_reprovados = 0

if contador_nmr_aprovados > 0:
    print('\033[32mSobre os alunos aprovados: \033[m')
    for qtd in lista:
        if qtd['Média'] >= 5:
            print(f'O aluno \033[33m{qtd["Nome"]}\033[m foi aprovado com a média \033[33m{qtd["Média"]}\033[m.')
            contador_aprovados += 1   
    print('~-~'*40)
if contador_nmr_reprovados > 0:
    print('\033[31mSobre os alunos reprovados: \033[m')
    for qtd in lista:
        if qtd['Média'] < 5:
            print(f'O aluno \033[33m{qtd["Nome"]}\033[m foi reprovado com a média \033[33m{qtd["Média"]}\033[m.')
            contador_reprovados += 1
    print('~-~'*40)        
print(f'Analisamos ao todo \033[33m{cont} alunos.\033[m')
print('~-~'*40)
if contador_reprovados > 0:
    print(f'De {cont} alunos (as), \033[31m{contador_reprovados} alunos (as) foram reprovados (as).\033[m ')
else:
    print('\033[32mNenhum aluno (a) foi reprovado (a).\033[m')
    
print('~-~'*40)

if contador_aprovados > 0:
    print(f'De {cont} alunos (as), \033[32m{contador_aprovados} alunos (as) foram aprovados (as).\033[m ')
else:
    print('\033[31mNenhum aluno (a) foi aprovado (a).\033[m')