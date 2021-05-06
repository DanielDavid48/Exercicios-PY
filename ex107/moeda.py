def metade(num):
    metade1 = num / 2
    return metade1

def dobro(num):
    dobro1 = num * 2
    return dobro1

def aumentando(num, taxa=0):
    dezporcento = taxa / 100 * num
    final = num + dezporcento
    return final

def diminuindo(num, taxa=0):
    trezeporcento = taxa / 100 * num
    final1 = num - trezeporcento
    return final1
