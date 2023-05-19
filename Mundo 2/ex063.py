'''
fibonachi
'''
print('-'*23)
print('SEQUENCIA DE FIBONACCI')
print('-'*23)
n = int(input('Tamanho da sequencia: '))
print('~'*23)
t1 = 0
t2 = 1
print('{} - {}'.format(t1,t2),end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*23)

