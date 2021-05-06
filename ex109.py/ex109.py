import moeda

n = float(input('Digite o preço: R$ '))
print(f"""A metade de \033[33m{moeda.moeda(n)}\033[m é \033[33m{moeda.metade(n, True)}\033[m
O dobro de \033[33m{moeda.moeda(n)}\033[m é \033[33m{moeda.dobro(n, True)}\033[m
Adicionando 10% em \033[33m{moeda.moeda(n)}\033[m resulta em \033[33m{moeda.aumentando(n, True)}\033[m
Retirando 13% de \033[33m{moeda.moeda(n)}\033[m resulta em \033[33m{moeda.diminuindo(n, True)}\033[m""")