from datetime import date
atual=date.today().year
ano=int(input('Ano de Nascimento:'))
idade=atual-ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')


