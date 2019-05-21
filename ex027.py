nome=str(input('Digite seu nome completo:')).strip()
n=nome.split()

print('muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu útimo nome é {}'.format(n[len(n)-1]))
