from random import randint

computador=(randint (1, 10),randint (1, 10),randint (1, 10),randint (1, 10),randint (1, 10))
print('Os valores sorteados foram: ', end='')
for c in computador:
    print(f'{c} ',end='')

print(f'\nO maior valor sorteado foi {max(computador)}')
print(f'O menor valor sorteado foi {min(computador)}')



