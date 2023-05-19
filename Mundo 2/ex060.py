num = int(input('Digite o numero: '))
fator = int(1)
for i in range(num, 0,-1):
    fator = fator * i
    #print(fator)
print('A fatoração é: {}'.format(fator))

fator = int(1)
print('{}!'.format(num), end='  ')
while num >= 1:
    fator *= num
    print('{}'.format(num), end='')
    print(' x ' if num > 1 else ' = ', end='')
    num -= 1
print(' {}'. format(fator))