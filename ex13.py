print('Bem vindo, caro gestor de RH')
nome_funcionario = input('Insira o nome do funcionário: ')
s = float(input('Insira aqui o valor de pagamento atual: R$'))

conta = s + (s * 15 / 100)

print(f'O funcionário {nome_funcionario} atualmente recebe {s} e com o aumento de 15% passará a receber R${conta:.2f}.')