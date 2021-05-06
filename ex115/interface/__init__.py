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

def line(tam = 42):
    return '-' * tam

def texto(msg):
    print(line())
    print(msg.center(42))
    print(line())

def menu(lista):
    texto('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opc = leia_int('\033[36mSua opção:\033[m ')
    return opc
