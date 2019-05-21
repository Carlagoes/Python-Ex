largura=float(input('Largura da parede:'))
altura=float(input('Altura da parede:'))
area=largura*altura
print('Sua parede tem a dimensão de {}x{} e sua áre de é de {}m².'.format(largura,altura,area))
tinta=area/2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))

