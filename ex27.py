print('Bem vindp')
nome = str(input('Insira seu nome completo: ')).strip()

# pegando o primeiro nome

primeiro_nome = nome.split()
primeiro_nome1 = (primeiro_nome[0])

# pegando o ultimo nome

ultimo_nome = nome.split()
ultimo_nome1 = (ultimo_nome[len(ultimo_nome)-1])

print(f"""Prazer em te conhecer {nome}
Seu primeiro nome é {primeiro_nome1}
Seu último nome é {ultimo_nome1}""")