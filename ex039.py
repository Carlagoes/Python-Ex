from datetime import date
atual=date.today().year
data=int(input('Ano de nascimento:'))
idade=atual-data
print('Quem nasceu em {} tem {} anos em {}.'.format(data,idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo=18-idade
    print('Você ainda não precisa se alistar. Ainda faltam {} anos para se alistar.'.format(saldo))
    ano=atual+saldo
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo=idade-18
    print('Você está atrasado! Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

