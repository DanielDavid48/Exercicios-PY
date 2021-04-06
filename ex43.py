print('Seja bem vindo ao SAUDE VITAL')
nome = str(input('Me informa seu nome: '))
print(f'\033[32mPrazer em te conhecer\033[m {nome}!')
peso = float(input('Me informe seu peso: '))
print(f'\033[32mOk, você pesa\033[m {peso} \033[32mkilos.\033[m')
altura = float(input('Me informe sua altura: '))

# calculando o immc
imc1 = altura * altura
imc = peso / imc1

if imc < 17:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mEXTREMAMENTE ABAIXO DO PESO IDEAL!\033[m')
    print(f'{nome}, recomendamos que procure um médico nutricionista \033[31mURGENTE!\033[m')

elif imc >= 17 and imc < 18.5:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mABAIXO DO PESO IDEAL!\033[m')
    print(f'{nome}, recomendamos que procure um médico nutricionista \033[31mO MAIS RÁPIDO POSSÍVEL!\033[m')

elif imc >= 18.5 and imc < 25:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[32mVOCÊ ESTÁ NO PESO IDEAL!\033[m')

elif imc >= 25 and imc < 30:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[33mACIMA DO PESO IDEAL!\033[m')
    print(f'{nome}, recomendamos que procure um médico nutricionista \033[31mO MAIS RÁPIDO POSSÍVEL!\033[m')

elif imc >= 30 and imc < 35:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mCOM OBESIDADE DE GRAU 1!\033[m')
    print(f'{nome}, recomendamos que procure um médico nutricionista \033[7;31mURGENTE!\033[m')

elif imc >= 35 and imc < 40:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mCOM OBESIDADE GRAU 2!\033[m')
    print(f'{nome}, recomendamos que procure um médico nutricionista \033[7;31mURGENTE!\033[m')

elif imc >= 40:
    print(f'{nome}, seu IMC é de {imc:.2f} e por isso você está \033[31mCOM OBESIDADE GRAU 3!\033[m')
    print(f'{nome}, recomendamos que procure um médico nutricionista \033[7;31mURGENTE\033[m')

else:
    print(f'{nome}, você não digitu uma opção váida!')