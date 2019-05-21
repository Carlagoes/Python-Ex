from time import sleep
p=int(input('Primeiro valor: '))
s=int(input('Segundo valor: '))
opção=0
while opção!=5:
    print('''[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa''')
    opção=int(input('>>>>>Qual é a sua opção? '))
    if opção==1:
        soma=p+s
        print('A soma entre {} + {} é {}'.format(p,s,soma))
    elif opção==2:
        produto=p*s
        print('O resultado de {} x {} é {}'.format(p,s,produto))
    elif opção==3:
        if p>s:
            maior=p
        else:
            maior=s
        print('Entre {} e {} o maior valor é {}'.format(p,s,maior))
    elif opção==4:
        print('Informe os números novamente: ')
        p=int(input('Primeiro valor: '))
        s=int(input('Segundo valor: '))
    elif opção==5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-'*15)
    sleep(2)
print('Fim do programa! Volte sempre!')
