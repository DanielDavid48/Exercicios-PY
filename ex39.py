

print('Seja bem vindo ao ALISTEI?')
nome = str(input('Informe seu nome: '))
print(f'Prazer em te conhecer {nome}!')
idade = int(input('Informe sua idade:  '))

# verificando
dia_alistamento = 17 - idade
atraso = idade - 18 

if idade < 17:
    print(f'{nome}, \033[32mvocê ainda não completou 18 anos, então deverá se alistar em {dia_alistamento} ano (s)!\033[m')

elif idade > 18:
    print(f'{nome}, \033[31mvocê passou do prazo de se alistar, você deveria ter se alistado à {atraso} ano (s) atrás!\033[m')

elif idade == 17:
    print(f'{nome}, \033[33mVocê deverá se alistar agora! Acesse o site da junta militar e se aliste!\033[m')