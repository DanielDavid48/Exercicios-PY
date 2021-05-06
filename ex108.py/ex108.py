import moeda

n = float(input('Insira um valor: '))
print(f"""A metade de \033[33m{n}\033[m é \033[33m{moeda.moeda(moeda.metade(n))}\033[m
O dobro de \033[33m{n}\033[m é \033[33m{moeda.moeda(moeda.dobro(n))}\033[m
Adicionando 10% em \033[33m{n}\033[m resulta em \033[33m{moeda.moeda(moeda.aumentando(n))}\033[m
Retirando 13% de \033[33m{n}\033[m resulta em \033[33m{moeda.moeda(moeda.diminuindo(n))}\033[m""")