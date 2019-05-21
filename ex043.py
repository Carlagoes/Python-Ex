peso=float(input('Qual é seu peso? (kg)'))
altura=float(input('Qual é sua altura? (m)'))
imc=peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do Peso Ideal')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está no Peso Ideal')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você está em Obesidade!')
else:
    print('Você está em Obesidade Mórbida, cuidado!')


