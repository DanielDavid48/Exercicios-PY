def notas(*num):
    notas = {}
    continuar = 's'
    cont = 0
    nt = 0
    notas["nota"] = []
    maior_nota = menor_nota = 0
    while continuar == 's':
        cont += 1
        notas1 = float(input(f'Informe a {cont}º nota: '))
        notas["nota"].append(notas1)
        if cont == 1:
            menor_nota = notas1
        nt += notas1
        if notas1 > maior_nota:
            maior_nota = notas["maior_nota"] = notas1
        if notas1 < menor_nota:
            menor_nota = notas["menor_nota"] = notas1
        continuar = input('Quer continuar [s/n]: ').lower()
    media_notas = nt / cont
    notas["media"] = media_notas
    notas["qtd_notas"] = cont
    print(f'Foram informadas \033[33m{cont} notas\033[m no total.')
    print(f'A média das notas ficou em \033[33m{media_notas:.2f}\033[m.')
    print(f'\033[33mA maior nota foi\033[m {maior_nota:.2f}')
    print(f'\033[33mA menor nota foi\033[m {menor_nota:.2f}')
    print(notas)
    if media_notas <= 3:
        print('\033[33mA situação da sala é deprovante!\033[m')
    elif media_notas > 3 and media_notas <= 5:
        print('\033[33mA situação da sala é ruim!\033[m')
    elif media_notas > 5 and media_notas <= 8:
        print('\033[36mA situação da sala é aceitável.\033[m')
    else:
        print('\033[32mA situação da sala é ótima!\033[m')
    
notas()