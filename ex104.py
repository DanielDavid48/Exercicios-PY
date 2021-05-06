def leia_int(msg):
    ok = False
    while True:
        inteiro = str(input(msg))
        if inteiro.isnumeric():
                print('Você digitou um número inteiro, parabens!')
                ok = True
        else:
            print('ERRO: Digite um numero inteiro válido: ')
        if ok:
            break
        
msg = leia_int('Digite um número: ')

