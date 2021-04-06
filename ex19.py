from random import choice

print('Seja bem vindo, vamos sortear?')

nome_prof = input('Para comecarmos, me informe seu nome, caro professor (a): ')

print(f'Prazer {nome_prof}, vamos sortear, me informa o nome dos alunos...')

aluno1 = input('Nome aluno 1: ')
aluno2 = input('Nome aluno 2: ')
aluno3 = input('Nome aluno 3: ')
aluno4 = input('Nome aluno 4: ')

lista_alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = choice(lista_alunos)

print(f'Olá professor (a) {nome_prof}, o aluno sorteado foi {sorteio}.')