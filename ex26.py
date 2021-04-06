print('Bem vindo')

frase = input('Insira uma frase: ')

# convertendo a string em maiusculas

mai = frase.upper()

# descobrindo quantas vezes aparece a letra A

qtd_a = mai.count('A')

# primeira vez que ele aparece

primeiro_lugar = mai.find('A')
adicionando_1 = primeiro_lugar + 1

# ultima vez que ela aparece

ultima_vez = mai.rfind('A')


print(f"""A letra "A" apareceu {qtd_a} vezes na frase.
A letra "A" apareceu a primeira vez na posição {adicionando_1}
A letra "B" apareceu pela ultima vez na posição {ultima_vez}""")

