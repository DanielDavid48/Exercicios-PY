import re

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

# Validando se a expressao comeca com ')'
fatiando_string_inicio = expressao1[0]
validacao_inicial = ')' in fatiando_string_inicio
if validacao_inicial == True:
    print(f'A expressão matemática {expressao1} é inválida!')

else:

    # validando se a expressão ta fechada com 2 ')',

    fatiando_string2 = expressao1[3:]
    validacao2 = '(' in fatiando_string2
    if validacao2 == True:
        agr_retirar = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z"
        del_characters = re.sub(agr_retirar, '', expressao1)
        del_characters2 = re.sub('[-+/?@#$%¨&*=]', '', del_characters)
        tirando_espacos_meio = del_characters2.split()
        juntando_string = ''.join(tirando_espacos_meio)
        lendo_string = len(juntando_string)
        if lendo_string % 2 == 0:
            verificar_1 = juntando_string.replace('(', '')
            lendo_qtd_parenteses = len(verificar_1)
            verificar_2 = juntando_string.replace(')', '')
            lendo_qtd_parenteses2 = len(verificar_2)
            if lendo_qtd_parenteses == lendo_qtd_parenteses2:
                fatiando_string3 = expressao1[-3:]
                validacao3 = ')))' in fatiando_string3
                if validacao3 == True:
                    print(f'A expressão que você digitou {expressao1} é inválida!')
                else:
                    print(f'A expressão {expressao1} é válida!')
                
            else:
                print(f'A expressão {expressao1} não é válida!')
        else:
            print(f'A expressão {expressao1} não está válida!')

