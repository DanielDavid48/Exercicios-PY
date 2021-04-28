
print('Seja bem vindo!')

matriz = [[[], [], []], 
          [[], [], []], 
          [[], [], []]]

for ax in range(0,3):    
    for ay in range(0, 3):
        matriz[ax][ay] =  int(input('Digite um valor: '))

for  ax in range(0,3):
    for ay in range(0,3):
        print(f'[{matriz[ax][ay]:^4}]', end='')
    print()