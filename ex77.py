tupla_palavras = ('Mariana', 'Abacaxi', 'Advogado', 'Beleza', 'Casa', 'Avestruz')
for palavra in tupla_palavras:
    print(f'\n{palavra.upper()} contém as vogais: ', end='')
    for letra in palavra:
        if letra.lower()  in 'aeiou':
            print(letra, end='')