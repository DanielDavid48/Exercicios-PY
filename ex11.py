print('Bem vindo ao FastWork')

alt = float(input('Insira a altura da parede em metros: '))
largura = float(input('Insira a largura da parede em metros: '))

area = alt * largura

#1L de tinta pintam 2m quadrados de parede
qt_tinta = area / 2


print(f'A sua área é de {area}m² e você precisará de {qt_tinta}L de tinta para pintar a parede por completo')
