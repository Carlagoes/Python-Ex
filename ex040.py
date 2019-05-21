n1=float(input('Primeira nota:'))
n2=float(input('Segunda nota:'))
média=(n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,média))
if média < 5.0:
    print('REPROVADO!')
elif média >= 5 and média < 7:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('APROVADO!')
