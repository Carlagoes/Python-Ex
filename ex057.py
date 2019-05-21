s=str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while s not in 'MmFf':
    s=str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'. format(s))

