lista = []
expressao = input('Digite uma expressão matemática: ').strip()
lista.append(expressao)

# AQUI EU PEGUEI A EXPRESSÃO DA LISTA
expressao1 = (lista[-1])

# AQUI EU LI O TAMANHO DESSA EXPRESSAO
lendo_expressao = len(expressao1)

# PRINT PRA UMA MELHOR EXECUCAO
print(f'Você digitou a expressão {expressao1}.')
print(f'Essa expressão tem {lendo_expressao} caracteres.')

# VALIDANDO SE A EXPRESSAO ESTA FECHADA COM APENAS 1 ')'
# SE ESTIVER, ELA É VERDADEIRA
fatiando_string = expressao1[-1]
validacao = ')' in fatiando_string

# VALIDANDO SE A EXPRESSAO ESTA FECHADA COM 2 ')', SENDO NENHUM DOS ')' UM FECHAMENTO DE UMA SUB-EXPRESSÃO
# SE ESTIVER, ELA É FALSA
#fatiando_string2 = expressao1[2:]
#validacao2 = '))' in fatiando_string2

# VALIDANDO SE A EXPRESSAO ESTA FECHADA COM 2 ')', SENDO UM DOS ')' UM FECHAMENTO DE UMA SUB-EXPRESSÃO
# SE ESTIVER, ELA É VERDADEIRA
#sublista = []
#fatiando_string2 = expressao1[3:]
#validacao2 = '))' in fatiando_string2
#cont = 0
#while validacao2 == True:
#    procurando = expressao1.rfind('(', 2, -1)
#    if procurando != 0:
#        procurando2 = expressao1.rfind(')', procurando, -2)
#        procurando = expressao1.rfind('(', procurando2, -2)
#        while procurando != 0:
#            procurando2 = expressao1.rfind(')', procurando, -2)
#            procurando = expressao1.rfind('(', procurando2, -2)
#            if procurando == False:
#                cont += procurando
#                print(f'teste{procurando}')
#                break
#        else:
#            print('Mensagem de teste')
#            break


# VALIDANDO SE A EXPRESSAO ESTA FECHADA COM 3 ')', SENDO 1 ')' FECHAMENTO DE UMA SUB-EXPRESSÃO 
# SE ESTIVER, ELA É FALSA
fatiando_string3 = expressao1[3:]
validacao3 = ')))' in fatiando_string3

# VALIDANDO SE A EXPRESSAO COMEÇA COM '('
# SE ESTIVER ELA É VERDADEIRA
fatiando_string4= expressao1[0]
validacao4 = '(' in fatiando_string3

# VALIDACAO DA EXPRESSAO
if validacao4 == True and validacao3 == True:
    print('Sua expressão é inválida!')
    
elif validacao4 == True and validacao == True:
    print('Sua expressão é válida!')
    
else:
    print('em construção...')