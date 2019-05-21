from math import radians, sin, cos, tan
ang=float(input('Digite o angulo que você deseja:'))
s=sin(radians(ang))
c=cos(radians(ang))
t=tan(radians(ang))
print('O angule de {} tem o seno de {:.2f}.'.format(ang,s))
print('O angulo de {} tem o cosseno de {:.2f}.'.format(ang,c))
print('O angulo de {} tem o tangente de {:.2f}.'.format(ang,t))