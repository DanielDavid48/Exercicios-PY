try:
    nome = int(input('insira um número: '))
except:
    print('Não é um número!')
else:
    print(f'{nome} é um número!')