from random import randint

tupla = (randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999), randint(1, 999))        
maior = max(tupla)
menor = min(tupla)

print(f'Os números escolhidos foram \033[33m{tupla}\033[m, nela o maior número é \033[33m{maior}\033[m e o menor é \033[33m{menor}\033[m.')