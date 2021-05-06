#frase = 'Curso em video python'
#print(frase.replace('python', 'andoid'))

#print("""Pentest "penetration test" é o ato de achar falhas em sistemas, a área que foca nisso 
#é Redes, porém isso está dentro do aspecto da ciência da computação e desenvolvimento de sistemas, 
#alguém que decide realizar pentest precisa saber programar no mesmo nível de
#um dev ou não vai sair do lugar, para invadir é necessário noção de como construir.""")

########################################################################################################################

# desafio 1: Crie um programa que leia um nome completo de uma pessoa e mostre: o nome com todas as letras maiusculas; 
# o nome com todas minusculas; quantas letras ao todo sem considerar espaços; quantas letras tem o primeiro nome

# incio



#print('Seja bem vindo')
#nome = input('Insira seu nome: ')

# Nome todo minusculo e maiusculo

#nome_todo_maiusculo = nome.upper()
#nome_todo_minusculo = nome.lower()

# Quantidade de letras sem espaco

#nome1 = nome.split()
#nome3 = ''.join(nome1)
#nome4 = len(nome3)

# Quantidade de letras do primeiro nome >>

#qtd_primeiro_nome = nome.split()
#qtd1 = (qtd_primeiro_nome[0])
#qtd2 = len(qtd1.strip())

#print(f'O nome {nome} todo maisculos fica:') 
#print(f'>>> {nome_todo_maiusculo}')
#print('----------------------------------------')
#print('Todo minusuculo fica:')
#print(f'>>> {nome_todo_minusculo}')
#print('----------------------------------------')
#print(f'O nome {nome} contém:')
#print(f'>>> {nome4} letras sem considerar espaços')
#print('----------------------------------------')
#print(f'>>> O primeiro nome de {nome} contém {qtd2} letras')


##########################################################################################################################3

# desafio 2: Faca um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex: digite um numero: 1834
#unidade: 4; dezena: 3; centena: 8 e milhar: 1

#print('Seja bem vindo')

#num = int(input('Insira um número: '))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000% 10

#print(f"""Analisando o número {num}
#Unidade: {u}
#Dezena: {d}
#Centena: {c}
#Milhar: {m}""")

########################################################################################################################

# desafio 3: Crie um programa que leia um nome de uma cidade e diga se ela começa ou nao com o nome santo.

#print('Minha cidade começa com Santo?')
#nome_cidade = input('Insira o nome da cidade: ')

# letra maiuscula 

#primeira_palavra = nome_cidade.split()
#primeira_palavra1 = (primeira_palavra[0])

# letra minuscula

#primeira_palavra_maiuscula = nome_cidade.split()
#primeira_palavra_maiuscula2 = (primeira_palavra_maiuscula[0])

#if primeira_palavra1 == 'santo':
    #print('Sim, sua cidade começa com Santo.')

#elif primeira_palavra_maiuscula2 == 'Santo':
    #print('Sim, sua cidade começa com Santo.')

#else:
    #print('Sua cidade não começa com Santo.')

#######################################################################################################################

################################################################################################################

# desafio 4: crie um programa que leia o nome de uma pessoa e diga se ele tem silva no nome,

#print('Meu nome tem Silva?')
#nome = input('Insira seu nome completo: ')

# procurando silva na string nome

#nome1 = nome.find('Silva')
#nome2 = nome.find('silva')

#if nome1 >= 0:
#    print('Sim, seu nome tem Silva.')

#elif nome2 >= 0:
#    print('Sim, seu nome tem Silva.')

#else:
#    print('Não, seu nome não tem Silva.')

#################################################################################################################333

# Desafio 5: faca um programa que leia a frase pelo teclado e mostre: quantas vezes aparece a letra A; Em que posição
#ela aparece pela primeira vez e em que posicao ela aparce peela ultima vez

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

