def área(largura, comprimento):
    a=largura*comprimento
    print(f'A área do terreno é de {largura}x{comprimento} é de {a}m2.')


print(' Controle de Terrenos ')
print('-'*30)
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
área(l,c)
