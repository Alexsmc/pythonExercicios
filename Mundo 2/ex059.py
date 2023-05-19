def somar(a,b): #função responsável por somar.
    resultado = a + b
    print('SOMA DE {} + {} = {}'.format(a,b,resultado))
    print('-='*20,'\n')

def multiplicar(a,b): #função responsável por multiplicar
    resultado = a * b
    print('SOMA DE {} x {} = {}'.format(a, b, resultado))
    print('-=' * 20,'\n')

def maior(a,b): #função responsavel por dizer qual o maior numero ou se são iguais
    if a > b:
        print('O numero {} é maior que o numero {}'.format(a,b))
        print('-=' * 20,'\n')
    elif b > a:
        print('O numero {} é maior que o numero {}.'.format(b,a))
        print('-=' * 20,'\n')
    else:
        print('Os numeros são iguais.')
        print('-=' * 20,'\n')


menu = 0
print('OLÁ! PRIMEIRO ESCOLHA DOIS NUMEROS:')
num1 = float(input('NUMERO 1: '))
num2 = float(input('NUMERO 2: '))

while menu != 5:
    print('''ESCOLHA UMA OPÇÃO ABAIXO
    [1] SOMAR
    [2] MULTIPLCAR
    [3] MAIOR
    [4] NOVOS NUMEROS
    [5] SAIR''')
    menu = int(input('ESCOLHA UMA OÇÃO: '))
    if menu == 1:
        somar(num1, num2)
    elif menu == 2:
        multiplicar(num1,num2)
    elif menu == 3:
        maior(num1,num2)
    elif menu == 4:
        num1 = float(input('NUMERO 1: '))
        num2 = float(input('NUMERO 2: '))
    elif menu >5:
        print('Opção Inválida')

print('PROGRAMA FINALIZADO!')
