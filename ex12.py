print('Bem vindo ao PORCENTAGEM SIMPLIFICADA')
v = float(input('Insira o valor do produto: R$'))


valor_com_desconto = v - (v * 5 / 100)

print(f'O produto custa {v} e com os 5% de desconto, ele passará a custar {valor_com_desconto:.2f}')