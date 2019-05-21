v=s=c=0
while True:
  v=int(input('Digite um valor (999 para parar): '))
  if v==999:
      break
  c+=1
  s+=v
print(f'A soma dos {c} valores foi {s}!')
