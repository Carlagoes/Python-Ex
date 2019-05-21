preço=float(input('Qual o preço do produto? R$'))
desconto=preço-(preço*5/100)
print('O produto que custava {:.2f}, na promoção com desconto de 5% vai custar {:.2f}'.format(preço, desconto))

