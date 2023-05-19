extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')

#while True:
valor = int(input('Digite um numero entre 0 e 20: '))
while (valor < 0) or (valor > 20):
    print('Tente novamente')
    valor = int(input('Digite um numero entre 0 e 20: '))
print(f'Você digitou o numero {extenso[valor]}')