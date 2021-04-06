print('\033[32mSeja bem vindo ao TABUADA SIMPLES!\033[m')

n = int(input('Insira um número: '))
for x in range(0, 11):
    conta = n * x
    print(conta)