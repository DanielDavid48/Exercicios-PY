from datetime import date

lista_maiores18 = []
lista_menores18 = []

for x in range(7):
    nascimento = int(input('Insira o ano de nascimento: '))
    ano = date.today().year
    calculo = ano - nascimento
    if calculo >= 18:
        lista_maiores18.append(calculo)

    elif calculo < 18:
        lista_menores18.append(calculo)

lendomais18 = (len(lista_maiores18))
lendomenos18 = (len(lista_menores18))

print(f'{lendomais18} pessoas tem 18 anos ou mais, cuja idades são {lista_maiores18}.')
print(f'{lendomenos18} pessoas ainda são menores de idade, cuja iades são {lista_menores18}.')
