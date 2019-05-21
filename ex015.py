aluguel=int(input('Quantos dias alugados?'))
km_rodado=int(input('Quantos km rodados?'))
custo_dia=60
custo_km=0.15
preço=(aluguel*custo_dia)+(km_rodado*custo_km)
print('O total a pagar é de R${:.2f}'.format(preço))
