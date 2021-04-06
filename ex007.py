
print('Seja bem vindo, informe seu nome por gentileza!')
nome_professor = input('Insira seu primeiro nome: ')
print(f'Que bom vê-la (o) novamente por aqui, querida (o) {nome_professor}')
nome_aluno = input('Insira o primeiro nome do aluno: ')
print(f'Ok, achei aqui o aluno {nome_aluno}')
print(f'Agora vamos calcular a média do seu aluno {nome_aluno}')

#notas dos alunos

nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))
nota5 = float(input('Insira a quinta nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

if media >= 5:
    print(f'Parabéns, o {nome_aluno}, foi aprovado')
    print(f'A média foi de {media} pontos.')

else:
    print(f'Caro {nome_professor}, infelizmente o aluno {nome_aluno} não foi aprovado.')
    print(f'A média foi de {media} pontos.')
