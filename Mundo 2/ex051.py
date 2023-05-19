'''
crie um programa que leia uma PA até 10
'''
print('='*30)
print('     10 TERMOS DE UMA PA    ')
print('='*30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for c in range(10):
    print(termo, end=' -> ')
    termo = termo + razao
print('ACABOU')