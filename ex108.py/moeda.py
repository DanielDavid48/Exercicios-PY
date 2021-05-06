
def metade(num=0):
    meio = num / 2
    return meio

def dobro(num=0):
    dobro1 = num * 2
    return dobro1

def aumentando(num=0):
    dezporcento = 10 / 100 * num
    final = num + dezporcento
    return final

def diminuindo(num=0):
    trezeporcento = 13 / 100 * num
    final1 = num - trezeporcento
    return final1

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
