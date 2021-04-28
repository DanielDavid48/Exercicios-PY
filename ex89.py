lista = [] # lista principal
dados = [] # lista de transição
continuar = ''
cont = 1
contador_for = 0
contador_qtd_elementos = 0
while continuar == '':
    print(f'\033[36m           {cont}º ALUNO                  \033[m')
    nome = input('Insira o nome do aluno: ')
    nota1 = float(input(f'Insira a 1° nota do aluno {nome}: '))
    nota2 = float(input(f'Insira a 2° nota do aluno {nome}: '))
    lista.append(dados[:])
    dados.append(nome) # coleta do nome e inserção na lista de transição
    lista[contador_for].append(dados[:]) # Inserindo o nome na lista principal à partir da de transição
    dados.clear() # Limpando a lista de transição
    dados.append(nota1) # coleta da primeira nota e inserção na lista de transição
    dados.append(nota2) # coleta da segunda nota e inserção na lista de transição
    lista[contador_for].append(dados[:]) # inserção das notas na lista principal à partir da de transição
    dados.clear() # limpando a lista de transição
    media = (nota1 + nota2) / 2 # calculando a média
    dados.append(media) # coleta da media e inserção na lista de transição
    lista[contador_for].append(dados[:]) # inserindo a media na lista principal à partir da de transição
    dados.clear() # limpando a lista
    continuar = input('Para continuar: ENTER | Para sair digite: 0 ').lower()
    while continuar not in "''0":
        print('\033[31mOpção inválida!\033[m')
        continuar = input('Para continuar: ENTER | Para sair digite: 0 ').lower()
    cont += 1
    contador_for += 1
    contador_qtd_elementos += 1

print(f'nº          aluno                      media')
for x in range(0, contador_qtd_elementos):
    print(f'{x}   |   {lista[x][0]}     |     {lista[x][2]}')