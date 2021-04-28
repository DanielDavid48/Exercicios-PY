print('Seja bem vindo!')
prof = input('Insira seu nome para continuar: ')
print(f'\033[36mQue prazer te conhecer querida (o) {prof}!\033[m')
print('\033[33mVamos ao trabalho então :D\033[m')

lista = [] # lista principal
dados = [] # lista de transição
continuar = ''
cont = 1
contador_for = 0
contador_qtd_elementos = 0
while continuar == '':
    print(f'\033[36m========== {cont}º ALUNO ==================\033[m')
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

print(f'\033[33m Nº                      ALUNO                                       MÉDIA\033[m')
for x in range(0, contador_qtd_elementos):
    
    listaa = str(lista[x][0]).replace('[','').replace(']','')#Remove os colchetes
    listaa2 = str(lista[x][2]).replace('[','').replace(']','')#Remove os colchetes
    
    print(f'{x:^4} |{listaa:^40}| {listaa2:^50}')#:^5 tentei usar pra centralizar, mas isso não deu muito certo, por conta dos nomes com muitos caracteres.

ver_notas = input('\033[33mQuer ver notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')
while ver_notas not in "''0":
    print('\033[31mOpção inválida!\033[m')
    ver_notas = input('\033[33mQuer ver mais notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')
if ver_notas == '':        
    while ver_notas == '':
        print('\033[33mDICA: O número do aluno está antes do nome no resumo de médias!\033[m')
        aluno = int(input('Insira o n° do aluno escolhido: '))
        listaa3 = str(lista[aluno][1]).replace('[','').replace(']','')#Remove os colchetes
        listaa4 = str(lista[aluno][0]).replace('[','').replace(']','')#Remove os colchetes
        print(f'As notas do aluno (a) {listaa4} são: {listaa3}.')
        ver_notas = input('\033[33mQuer ver mais notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')
        while ver_notas not in "''0":
            print('\033[31mOpção inválida!\033[m')
            ver_notas = input('\033[33mQuer ver mais notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')

else:
    print(f'Tudo bem. Finalizando programa....')

print(f'Tudo bem, foi um prazer encontrá-la por aqui querida (o) {prof}!')
print('Programa finalizado!')