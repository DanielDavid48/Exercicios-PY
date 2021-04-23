#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

import datetime, sys
from time import sleep
from os import linesep

nome_cliente = input(f'Olá, bem vindo ao Banco do mundo da fantasia.{linesep}Insira o seu nome para continuar: ')
senha_cliente = input(f'Insira a sua senha, {nome_cliente}: ')
print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Logando no sistema bancário...")
print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Checando credenciais...{linesep}Usuário: {nome_cliente}{linesep}Senha: {senha_cliente}")
sleep(2)
print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Logado com sucesso!")
print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Que bom te ter aqui {nome_cliente}")

while True:
    serviço = int(input(f'Escolha um serviço inserindo o número equivalente a ele, para podermos prosseguir.{linesep}[1] - Saque{linesep}[2] - Finalizar Serviço{linesep}Digite aqui o número: '))

    if serviço == 2:
        sys.exit()
    elif serviço == 1:
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Acessando sistema de saque...")
        sleep(2)    
        valor = int(input(f'{nome_cliente}, quanto você deseja sacar?{linesep}Insira aqui o valor: '))
        cedulas50 = valor // 50
        cedulas20 = (valor - 50 * cedulas50) // 20
        cedulas10 = ((valor - 50 * cedulas50) - 20 * cedulas20) // 10
        cedulas1 = (((valor - 50 * cedulas50) - 20 * cedulas20) - 10 * cedulas10) // 1
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Realizando saque")
        sleep(1)
        print(f"{linesep}Com R${valor} é possível sacar:{linesep}{cedulas50} cédulas de R$50{linesep}{cedulas20} cédulas de R$20{cedulas10} cédulas de R$10{linesep}{cedulas1} cédulas de R$1")
        sleep(1)
    else:
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Opção inválida, finalizando sessão!")
        sleep(1)
        sys.exit()
    finalizarPrograma = int(input(f'Deseja continuar? [1] - Sim | [2] - Não{linesep}Insira aqui o número: '))
    
    if finalizarPrograma != 1:
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] | Finalizar !")
        sys.exit()