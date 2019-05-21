time='Ceará SC','Palmeiras','Athletico PR','Flamengo','São Paulo','Chapecoense','Bahia','Atletico','Santos','Goias','Corintias','Avai','Grêmio','Fluminense','Cruzeiro','Internacional','Botafogo','Vsco da Gama','Fortaleza','CSA'


print('-='*20)
print(f'Lista de times do Brasileirão: {time}')
print('-='*20)
print(f'Os 5 primeiros são {time[0:5]}')
print('-='*20)
print(f'Os 4 últimos são {time[-4:]}')
print('-='*20)
print(f'Os times em ordem alfabéticas são {sorted(time)}')
print('-='*20)
print(f'O Chapecoense está na {time.index("Chapecoense")+1}ª posição ')
