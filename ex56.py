

lista_idades_fem = []
lista_idades_mas = []
lista_nomes_fem = []
lista_nomes_mas = []
lista_sexo_masc = []
lista_sexo_femi = []

for nome in range(4):
    nome = str(input('Insira o nome da pessoa: '))
    idade = int(input(f'Insira a idade do {nome}: '))
    sexo = str(input(f"""Agora informe o sexo do {nome}, coloque 
m para masculino e f para feminino: """))
    print('\033[33m=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\033[m')
    
    if sexo == 'f':
        lista_sexo_femi.append(sexo)
        lista_idades_fem.append(idade)
        lista_nomes_fem.append(nome)

    if sexo == 'm':
        lista_sexo_masc.append(sexo)    
        lista_idades_mas.append(idade)
        lista_nomes_mas.append(nome)

# calculando a media
media_idades = sum(lista_idades_mas)
media_idades1 = sum(lista_idades_fem)
media_idades2 = media_idades + media_idades1 
media_idades3 = media_idades2 / 4

print('\033[33mAnalisando os dados que você inseriu:\033[m')

# nome do homem mais velho
lendo_idade_homens = len(lista_idades_mas)
if lendo_idade_homens > 0:
    idade_homem_mais_velho = max(lista_idades_mas)
    recorte = lista_idades_mas.index(idade_homem_mais_velho)
    nome_homem_mais_velho = lista_nomes_mas[recorte]
    print(f"""\033[33m=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\033[m
O homem mais velho tem {idade_homem_mais_velho} anos e o nome dele é {nome_homem_mais_velho}""")

# qtd mulheres com menos de 20 anos
lista = list(filter(lambda x: x <= 20, lista_idades_fem))
lendo_qtd = len(lista)

print(f"""\033[33m=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\033[m
A média de idade do grupo é de {media_idades3}.
\033[33m=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-=\033[m
Por último, há {lendo_qtd} mulheres com menos de 20 anos.""")

