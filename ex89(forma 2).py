import time

print('Seja bem vindo!')
prof = input('Insira seu nome para continuar: ')
print(f'\033[36mQue prazer te conhecer querida (o) {prof}!\033[m')
time.sleep(1)
print('\033[33mVamos ao trabalho então :D\033[m')
time.sleep(1)

lista = [] 
continuar = ''
contador_alunos = 1
contador_qtd_elementos = 0

while continuar == '':
    print(f'\033[36m==================== {contador_alunos}º ALUNO ==========================\033[m')
    nome = input('Insira o nome do aluno: ')
    nota1 = float(input(f'Insira a 1° nota do aluno {nome}: '))
    nota2 = float(input(f'Insira a 2° nota do aluno {nome}: '))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1, nota2], media])
    continuar = input('Para continuar: ENTER | Para sair digite: 0 ').lower()
    while continuar not in "''0":
        print('\033[31mOpção inválida!\033[m')
        continuar = input('Para continuar: ENTER | Para sair digite: 0 ').lower()
    contador_alunos += 1
    contador_qtd_elementos += 1

print(f'\033[33m Nº                   ALUNO                                      MÉDIA\033[m')
for x in range(0, contador_qtd_elementos):
    # removendo os colchetes dos nomes e médias
    listaa = str(lista[x][0]).replace('[','').replace(']','')
    listaa2 = str(lista[x][2]).replace('[','').replace(']','')
    
    # imprimindo os resultados
    print(f'{x:^4} |{listaa:^40}| {listaa2:^40}')

ver_notas = input('\033[33mQuer ver notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')
while ver_notas not in "''0":
    print('\033[31mOpção inválida!\033[m')
    ver_notas = input('\033[33mQuer ver mais notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')

if ver_notas == '':        
    while ver_notas == '':
        print('\033[33mDICA: O número do aluno está antes do nome no resumo de médias!\033[m')
        aluno = int(input('Insira o n° do aluno escolhido: '))
        # retirando os colchetes do nome e da nota do aluno escolhido
        listaa3 = str(lista[aluno][1]).replace('[','').replace(']','')
        listaa4 = str(lista[aluno][0]).replace('[','').replace(']','')
        # imprimindo o resultado
        print(f'As notas do aluno (a) {listaa4} são: {listaa3}.')
        # opcao de ver notas de outros alunos ou finalizar o programa
        ver_notas = input('\033[33mQuer ver mais notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')
        while ver_notas not in "''0":
            print('\033[31mOpção inválida!\033[m')
            ver_notas = input('\033[33mQuer ver mais notas de algum aluno?\033[m\nPara ver: \033[33mENTER\033[m | Para finalizar: \033[33m0\033[m    ')

else:
    print(f'\033[33mTudo bem. Finalizando programa....\033[m')

print('\033[36m=\033[m'*70)
print(f'Tudo bem, foi um prazer encontrá-la por aqui querida (o) {prof}!')
print('Programa finalizado!')