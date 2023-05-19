'''
Façá um programa q le uma frase e diz se ela é palindromo
'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase {} é um Palíndromo.'.format(frase))
    print('pois ao contrário fica: {}'.format(inverso))
else:
    print('A frase {}, não é um palíndromo \npois seu inverso é: {}'.format(frase,inverso))

#Fatiamento inverso[::-1]