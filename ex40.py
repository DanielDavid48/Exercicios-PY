print('Seja bem vindo à escola Costa Braga!')
nome_professor = str(input('Professor (A) me informe seu nome: '))
print(f'Ok, que bom vê-lo novamente {nome_professor}!')
nome_aluno = str(input('Me informe o nome do aluno: '))
print(f'Ok, achei o aluno {nome_aluno} aqui no sistema!')

# medias
media1 = float(input('Insira a primeira nota: '))
media2 = float(input('Insira a segunda nota: '))
media3 = float(input('Insira a terceira nota: '))
media4 = float(input('Insira a quarta nota: '))
media5 = float(input('Insira a quinta nota: '))

# contando a media
media_all = (media1 + media2 + media3 + media4 + media5)/5

if media_all < 5.0:
    print(f'Caro prefossor (a) {nome_professor}, o aluno  {nome_aluno} foi \033[31mreprovado!\033[m')

elif media_all >= 5.0 and media_all < 6.9:
    print(f'Caro professor (a), o aluno (a) {nome_aluno} deverá fazer uma \033[33mrecuperação!\033[m')

elif media_all > 7.0:
    print(f'Caro professor (a), o aluno (a) {nome_aluno} foi \033[32maprovado!\033[m')