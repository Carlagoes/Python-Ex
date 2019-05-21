valores=[[], []]
valor=0
for c in range(1,8):
    valor=int(input(f'Digite o {c}° valores: '))
    if valor%2==0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print('-='*20)
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')


