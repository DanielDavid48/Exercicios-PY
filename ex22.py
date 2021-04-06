print('Seja bem vindo')
nome = input('Insira seu nome completo: ')

# nome em maiusculos
ma = nome.upper()

# nome em minusculos
mi = nome.lower()

# qtd Letras sem espacos
qtd1 = nome.split()
qtd2 = ''.join(qtd1)
qtd3 = len(qtd2)

# qtd primeiro nome
qtd_1 = nome.split()
qtd_2 = (qtd_1[0])
qtd_3 = len(qtd_2)

print(f"""Analisando seu nome....
>>>
Seu nome todo maiusculo fica:
>>> {ma}
-----------------------------------------
Seu nome todo minusculo fica:
>>> {mi}
------------------------------------------
Total de letras desconsiderando os espaços:
>>> {qtd3}
------------------------------------------
Total de letras do seu primeiro nome:
>>> {qtd_3}
------------------------------------------""')

