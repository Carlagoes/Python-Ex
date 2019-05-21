print('-'*20)
print('LOJA SUPER BARATÃO')
print('-'*20)

total=totmil=menor=cont=0
barato=' '
while True:
    prod=str(input('Nome do Produto: '))
    preço=float(input('Preço: R$' ))
    cont +=1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato=prod
    resp=' '
    while resp not in 'SN':
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp=='N':
        break

print('Fim do Programa')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')

