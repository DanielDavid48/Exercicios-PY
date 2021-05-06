import datetime

def voto():
    anos_atual = datetime.date.today().year
    nasc = anos_atual - nascimento

    if nasc < 16:
        return f'Com {nasc} anos: VOTO NEGADO'
    
    elif nasc >= 16 and nasc < 18:
        return f'Com {nasc} anos: VOTO OPCIONAL'
    
    elif nasc >= 18 and nasc < 65:
        return f'Com {nasc} anos: VOTO OBRIGATÓRIO'
    
    elif nasc >= 65:
        return f'Com {nasc} anos: VOTO OPCIONAL'

nascimento = int(input('Insira seu ano de nascimento: '))
voto1 = voto()
print(voto1)