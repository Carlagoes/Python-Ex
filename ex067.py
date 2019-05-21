while True:
    t=int(input('Quer ver a tabuada de qual valor? '))
    if t<0:
        break
    print('-'*30)
    for c in range (1,11):
        print(f'{t} x {c} = {(t*c)}')
    print('-'*30)
print('Programa tabuada encerrado. Volte sempre!')
