from datetime import date

print('Seja bem vindo à CONFEDERAÇÃO DE ESPORTES!')
nome = str(input('Me informe seu nome por gentileza: '))
print(f'Que prazer em te conhecer {nome}')
idade = int(input('Me informe somente o ano que você nasceu: '))

conta_idade = date.today().year - idade

if conta_idade <= 9:
    print(f'{nome}, a sua categoria é \033[34mmirim!\033[m')
 
elif conta_idade > 9 and conta_idade <= 14:
    print(f'{nome}, a sua categoria é \033[36minfantil\033[m')

elif conta_idade > 14 and conta_idade <= 19:
    print(f'{nome}, a sua categoria é \033[33mjúnior\033[m')

elif conta_idade > 19 and conta_idade <= 20:
    print(f'{nome}, a sua categoria é \033[32msênior\033[m')

elif conta_idade > 20:
    print(f'{nome}, a sua categoria é \033[35mmaster\033[m')