'''
Faça um programa que leia um numero e mostre sua tabuada até 10
'''

n = int(input('Qual numero de tabuada você desejaria ver? '))
for c in range(0,11):
    print('{} x {:2} = {}'.format(n,c,(c*n)))