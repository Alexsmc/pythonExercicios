# Crie um programa que leia um numero e mostre o seu
# dobro, triplo e raiz quadrada.

a = int(input('Manda um número: '))
dobro = a * 2
triplo = a * 3
raiz = a ** (1/2)

print('O numero é: {}.'.format(a))
print('O dobro é: {}\nO triplo é: {}\nA Raiz Quadrada é: {:.2f}'.format(dobro, triplo, raiz))
