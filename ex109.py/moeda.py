
def metade(num=0, show=False):
    meio = num / 2
    return meio if show == False else moeda(meio)

def dobro(num=0, show=False):
    dobro1 = num * 2
    return dobro1 if show == False else moeda(dobro1)

def aumentando(num=0, show=False):
    dezporcento = 10 / 100 * num
    final = num + dezporcento
    return final if show == False else moeda(final)

def diminuindo(num=0, show=False):
    trezeporcento = 13 / 100 * num
    final1 = num - trezeporcento
    return final1 if show == False else moeda(final1)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')
