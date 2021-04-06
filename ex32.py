from datetime import date

print('Esse ano é bissexto?')

ano = int(input('Insira o ano: '))

# verificando se o ano é bissexto

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto!')

else: 
    print(f'O ano {ano}, não é bissexto!')