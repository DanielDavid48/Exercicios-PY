import moeda

n = int(input('Insira um valor: '))
print(f"""A metade de \033[33m{n}\033[m é \033[33m{moeda.metade(n):.2f}\033[m
O dobro de \033[33m{n}\033[m é \033[33m{moeda.dobro(n):.2f}\033[m
Adicionando 20% em \033[33m{n}\033[m resulta em \033[33m{moeda.aumentando(n, 20):.2f}\033[m
Retirando 30% de \033[33m{n}\033[m resulta em \033[33m{moeda.diminuindo(n, 30):.2f}\033[m      
      """)