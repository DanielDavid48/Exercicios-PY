import datetime

ranking = ('América-MG', 'Athletico-PR', 'Atlético-GO', 'Atlético-MG', 'Bahia', 'Bragantino', 'Ceará', 
           'Chapecoense', 'Corinthians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 
           'Internacional', 'Juventude', 'Palmeiras', 'Santos', 'São Paulo', 'Sport')


# posicao da chapecoense
lugar = ranking.index('Chapecoense')

print(f"""\033[33mAnálisando a tabela do brasileirão hoje:\033[m
Os 5 primeiros colocados são {ranking[0:5]}
\033[36m~-~-~~-~-~~-~~-~~~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~\033[m
Os últimos 4 colocados da tabela são {ranking[16:]}
\033[36m~-~-~~-~-~~-~~-~~~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~\033[m
Os times em ordem alfabética são {sorted(ranking)}
\033[36m~-~-~~-~-~~-~~-~~~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~~-~-~-~\033[m
E o time da chapecoense está em {lugar + 1}° lugar na competição.""")