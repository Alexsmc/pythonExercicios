sexo = str(input('Digite o sexo: M/F ')).strip().upper()[0]
#print(sexo)
#while (sexo != 'M') and (sexo != 'F'):
while sexo not in 'MmFf':
    print('Valor incorreto, tente novamente')
    sexo = str(input('Digite o sexo: M/F ')).strip().upper()[0]
print('O sexo é {}'.format(sexo))

