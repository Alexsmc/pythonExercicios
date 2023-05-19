'''
Crie um programa que diga s eum numero é primo ou não
'''

n = int(input('Digite o numero: '))
r = int(0)
for c in range(1,n+1):
    if (n%c)==0:
        r += 1

if r > 2:
    print('Não é primo')
else:
   print('O numero {} é primo'.format(n))
