print('{:=^40}'.format(' LOJAS CARLA '))
compras=float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/ cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção=int(input('Qual é a opção?'))
if opção == 1:
    total = compras - (compras*10/100)
elif opção == 2:
    total = compras - (compras*5/100)
elif opção == 3:
    total = compras
    parcela= total/2
    print('Sua compra será parcelada em 2x de {:.2f} sem juros'.format(parcela))
elif opção == 4:
    total = compras +(compras*20/100)
    totparc=int(input('Quantas parcelas?'))
    parcela=total/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totparc,parcela))
else:
    total = compras
    print('Opção inválida de pagamento. Tente novamente!')
print('Sua compra de {:.2f} vai custar R${:.2f} no final.'.format(compras,total))
