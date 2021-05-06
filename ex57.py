s = str(input('Insira seu sexo: ')).lower()
while s[0] not in 'fm':
    s = str(input('Opçã inválida, digite novamente: ')).lower()

print('fim')