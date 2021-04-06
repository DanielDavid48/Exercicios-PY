frase = str(input('Insirama frase para verificar: '))

dicio = ['ó', 'ò', 'ô']

minu = frase.lower()
quero_trocar = dicio
trocar_por = "o"
frase = minu.replace(quero_trocar, trocar_por, len(frase))

a = minu
b = "!@#$-,.~´`^"
for char in b:
    a = a.replace(char,"")

frasejunta = a.split()
frasejunta1 = ''.join(frasejunta)

palindromo = frasejunta1 == frasejunta1 == frasejunta1[:: -1]
print(f'{frase} é palindrome?')

if palindromo == True:
    print(f'A frase {frase} é palindrome!')

elif palindromo == False:
    print(f'A frase {frase}, não é palindrome!')