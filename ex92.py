import datetime

print('Seja bem vindo ao \033[33mPosso me aposentar por tempo de trabalho?\033[m do INSS')

dicionario = {}
ano_atual = datetime.date.today().year

nome = dicionario['Nome'] = input('Informe seu nome por gentileza: ')
nascimento = int(input('Insira o ano do seu nascimento: '))
dicionario['Idade'] = ano_atual - nascimento
ctps = int(input('Insira o número da sua carteira de trabalho (Insira 0 senão tem!): '))
if ctps != 0:
    dicionario['CTPS'] = ctps
    ano_contratacao = dicionario['Ano de contratação'] = int(input('Insira o ano que você foi contratado: '))
    salario = dicionario['Salário'] = float(input('Insira seu salário atual: '))
    anos_trabalho = ano_atual - ano_contratacao
    anos_trabalho2 = ano_atual - (anos_trabalho - 35)
    anos_trabalho3 = (35 - anos_trabalho) + ano_atual 
    
    print('\033[32mGeramos um relatório:\033[m')
    print(f"""\033[33mSeu nome:\033[m {dicionario["Nome"]} 
\033[33mSua idade:\033[m {dicionario["Idade"]}
\033[33mSua carteira de trabalho:\033[m {dicionario["CTPS"]}
\033[33mSeu ano de contratação:\033[m {dicionario["Ano de contratação"]}
Você trabalha formalmente fazem \033[32m{anos_trabalho} anos.\033[m
\033[33mSeu salário atual:\033[m {dicionario["Salário"]}""")
    if anos_trabalho > 35:
        print(f'Você já pode se aposentar fazem {anos_trabalho - 40} anos, mais especificamente desde {anos_trabalho2}.')
    elif anos_trabalho == 35:
        print('Você já pode se aposentar à partir deste ano.')
    else:
        print(f'Você poderá se aposentar em {40 - anos_trabalho} anos, mais especificamente em {anos_trabalho3}.')
else:
    conta3 = ano_atual - nascimento
    conta3_1 = 65 - conta3
    conta4 = ano_atual + conta3_1
    if ano_atual - nascimento < 65:
        print('\033[32mGeramos um relatório:\033[m ')
        print(f"""\033[33mSeu nome:\033[m {dicionario["Nome"]}
\033[33mSua idade:\033[m {dicionario["Idade"]}
\033[33mComo você não tem CTPS (Carteira de trabalho), você não consegue verificar se pode se aposentar por tempo de trabalho!\033[m
Porém, poderá se aposentar por idade em {conta3_1} anos, mas especificamente em {conta4}.""")

    else:
        conta1 = (ano_atual - nascimento) - 65
        conta2 = ano_atual - conta1
        print('\033[32mGeramos um relatório:\033[m ')
        print(f"""\033[33mSeu nome:\033[m {dicionario["Nome"]}
\033[33mSua idade:\033[m {dicionario["Idade"]}
\033[33mComo você não tem CTPS (Carteira de trabalho), mas você tem mais de {ano_atual - nascimento} anos,
Você pode já se aposentar fazem {conta1} anos, mas especificamente desde {conta2}.\033[m""")