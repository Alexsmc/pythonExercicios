'''
cauculo IMC

18.5 abaixo do peso
18.5 e 25 peso ideal
25 - 30 sobrepeso
34 - 40 obesidade
40 - obesidade morbida
'''

peso = float(input('Qual seu peso?: '))
altura = float(input('Qual sua altura?: '))
imc = float(peso / (altura**2))

if imc > 0:
    if imc < 18.5:
        print('Você está ABAIXO DO PESO')
    elif 18.5 <= imc < 25:
        print('Você está no peso IDEAL')
    elif 25 <= imc < 30:
        print('Você está com SOBREPESO')
    elif 30 <= imc < 40:
        print('Você está com OBESIDADE')
    else:
        print('OBESIDADE MORBIDA')
else:
    print('Valor incorreto')

print('Seu IMC é de : {:.2f}'.format(imc))