print('Bem vindo ao Detran!')

nome_usuario = str(input('Informe seu nome: '))
print(f'Prazer em te conhecer {nome_usuario}!')
print('Vamos ver em que enrascada você se enfiou.')

print(f'{nome_usuario}, em que rodovia ocorreu isso?')
rodovia = str(input('A rodovia era: '))
print(f'E em qual cidade está localizada a rodovia {rodovia}?')
cidade = str(input('Fica localiada na cidade: '))
print(f'E a cidade {cidade}, fica em que estado?')
estado = str(input('Fica no estado: '))

print(f'{nome_usuario}, qual era a sua velocidade na rodovia {rodovia}?')
velocidade = int(input('Minha velocidade era: '))

# calculando a multa
if velocidade >= 80:
    conta_velocidade = velocidade - 80
    conta_velocidade1 = conta_velocidade * 7
    print(f"""===========================================
{nome_usuario}, veja o resumo do seu caso:
==========================================================
O caso ocorreu em: 

Rodovia: {rodovia}.
Cidade: {cidade}.
Estado: {estado}.
============================================================
O limite da via é de 80km/h.
Sua velocidade era de {velocidade}km/h.
E por isso você foi multado em R${conta_velocidade1:.2f} reais.
Tenha um bom dia e dirija com segurança!""")

else:
    print(f"""{nome_usuario}, veja o resumo do seu caso: 
=========================================================
A sua velocidade era de {velocidade}km/h e o limite
da via é de 80km/h, então você não foi multado.
Tenha um bom dia e dirija com segurança!""")