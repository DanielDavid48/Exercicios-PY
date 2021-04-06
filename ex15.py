import os

print('Seja bem viesndo ao CarLuguel')
print('Qual seu nome?')
nome_usuario = input('Insira seu nome aqui: ')
print('Qual carro você alugou?')
marca =input('Marca: ')
modelo = input('Modelo: ')
print('Quantos KM você rodou com o veículo?')
km = float(input('Insira aqui a resposta: '))
print('Você utilizou o veículo por quantos dias?')
dias = int(input('Insira aqui a resposta: '))

conta_dias = dias * 60
conta_km = km * 0.15
total_a_pagar = conta_dias + conta_km

print('------------------------------SISTEMA CARLUGUEL-----------------------------------------')
print(f'Olá {nome_usuario}, você utilizou o veiculo {modelo} da marca {marca} por {dias} dias.')
print('Visão geral do seu pedido:')
print(f'Carro {modelo} da marca {marca}')
print(f'Rodou com ele por {km} kilômetros')
print(f'Utilizou ele por {dias} dias')
print(f'A sua fatura fechou em R${total_a_pagar:.2f}')
print('---------------------------------------FIM------------------------------------------------')