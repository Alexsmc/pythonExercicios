from random import randint
from time import sleep
print('='*5,' ADIVINHE MEU PENSAMENTO','='*5)
num = randint(0,10)
jogador = str(input('DIGA SEU NOME APERTE ENTER PARA COMEÇAR:')).strip().upper()
print('\nOLÁ {}, ESTOU PENSANDO NUM NUMERO, AGUARDE...'.format(jogador))
sleep(1)
print('hum...')
sleep(1)
print('Ah ha!!! Duvido vc adivinhar!')
print('PENSEI EM UM NÚMERO ENTRE 1 E 10')
chute = 0
tentativa = 0
#print(num)
while chute != num:
    chute = int(input('Qual seu palpite? '))
    if chute > num:
        print('Menos...  tente de novo')
    elif chute < num:
        print('Mais... tente de novo.')
    tentativa += 1

print('PARABÉNS!!')
print('Você acertou o numero! {}'.format(num))
if tentativa == 1:
    print("Você leu meu pensamento? Acertou de primeira")
else:
    print('Você fez em {} tentativas'.format(tentativa))