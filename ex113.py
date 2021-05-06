def leia_int(msg):
    teste = False
    while teste == False:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            print('\033[33mUsuário preferiu não inserir um número.\033[m')
            num = 0
            teste = True
            return num
        except:
            print('\033[31mERRO! Insira um número inteiro válido!\033[m')
        else:
            teste = True
            return num
            
def leia_float(msg1):
    teste = False
    while teste == False:
        try:
            num1 = float(input('Insira um número real: '))
        except KeyboardInterrupt:
            print('\033[33mUsuário preferiu não inserir um número.\033[m')
            num1 = 0
            teste = True
            return num1
        except:
            print('\033[31mERRO! Insira um número real válido!\033[m')
        else:
            teste = True
            return num1
        
msg = leia_int('Digite um número inteiro: ')
msg1 = leia_float('Digite um número real: ')
print(f'O número inteiro foi {msg} e o real foi {msg1}.')