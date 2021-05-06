print('Seja bem vindo!')

def escreve(txt):
    tamanho = len(txt)
    print('='*tamanho)
    print(txt)
    print('='*tamanho)
    
escreve(input('Digite algo: '))