from random import randint
from time import sleep
computador = randint(0,5)  #Faz o pc pensar
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador=int(input('Em que número eu pensei?'))  #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você acertou! PARABÉNS!')
else:
    print('Você errou! Eu pensei no número {} e não no {}!'.format(computador, jogador))

