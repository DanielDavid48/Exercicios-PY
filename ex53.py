frase = str(input('Insirama frase para verificar: ')).upper()


a = frase
b = "!@#$-,.~´`^"
for char in b:
    a = a.replace(char,"")

frasejunta = a.split()
frasejunta1 = ''.join(frasejunta)

palindromo = frasejunta1 == frasejunta1 == frasejunta1[:: -1]
print(f'{frase} é palindrome?')

if palindromo == True:
    print(f'\033[32mA frase {frase} é palindrome!\033[m')

elif palindromo == False:
    print(f'\033[31mA frase {frase}, não é palindrome!\033[m')