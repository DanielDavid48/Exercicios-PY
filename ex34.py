print('Seja bem vindo ao RH!')

print('Qual o nome do funcionário? ')
funcionario = str(input('Nome: '))
print(f'Achei aqui o funcionário {funcionario}!')
print(f'Para prosseguirmos me informe o salário atual do {funcionario}, por gentileza.')
salario = float(input('Salário atual: R$ '))

# calculando o aumento
if salario > 1250:
    conta1 = salario * 10
    conta2 = conta1 / 100
    conta3 = salario + conta2
    print(f"""O funcionário {funcionario}, atualmente recebe R${salario} reais.
Com o aumento de 10% passará à receber R${conta3:.2f} reais mensais!""")

if salario <= 1250:
    conta4 = salario * 15
    conta5 = conta4 / 100
    conta6 = conta5 + salario
    print(f"""O funcionário {funcionario}, atualmente recebe R${salario} reais.
Com o aumento de 15% passará à receber R${conta6:.2f} reais mensais!""")

else:
    print('Parece que houve um erro, tente novamente!')