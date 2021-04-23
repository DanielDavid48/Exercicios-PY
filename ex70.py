import time

# guardando dados
valor_produtos = []
nome_produtos = []

continuar = ''
cont_produto = 0
cont = 0
# capturando dados
while continuar == '':
    print('\033[36m       SEJA BEM VINDO AO MINHACOMPRA.COM             \033[m')
    print(f'\033[34m               PRODUTO DE N°{cont + 1}            \033[m')
    nome_produto = input('Nome do produto: ')
    valor_produto = float(input(f'Qual o valor do {nome_produto}: R$'))
    cont_produto += valor_produto
    nome_produtos.append(nome_produto)
    valor_produtos.append(valor_produto)
    cont += 1
    continuar = input('Aperte ENTER para continuar ou 0 para sair: ')
    while continuar not in "''0":
        print('\033[31mInsira uma opção válida!\033[m')
        continuar = input('Aperte ENTER para continuar ou 0 para sair: ')
    
# filtrando os dados
# quantidade de produtos que custam mais de 1 mil reais
qtd_produtos_1k = list(filter(lambda x: x > 1000, valor_produtos))
filtrando_qtd = len(qtd_produtos_1k)

# nome do produto mais barato
valor_mais_barato = min(valor_produtos)
recorte = valor_produtos.index(valor_mais_barato)
produto_mais_barato = nome_produtos[recorte]

print('\033[33mAnalisando sua compra...\033[m')
time.sleep(1)
print(f"""Veja a análise de sua compra:
\033[36m=-=-=-=-==-=-=-==-=-==-=-==-=-=-=-=-==-==-=-=-=-=-==-=-==-=\033[m
O total da compra ficou em R${cont_produto:.2f} reais.
Há {filtrando_qtd} produtos em sua lista que custam mais de R$1.000.
O nome do produto mais barato é {produto_mais_barato} e ele custa R${valor_mais_barato:.2f} reais.
\033[36mEsses são os produtos analisados:\033[m
{nome_produtos}""")
