from random import randint


def sortear():
    num = []
    print('Numeros Sorteados!')
    for i in range(5):
        num.append(randint(1, 5))
        print(f'{num[i]}', end=', ')
    print()
    return num


def somar_par(valores):
    print('-='*20)
    par = 0
    print(f'Numeros pares: ')
    for i in valores:
        if i % 2 == 0:
            print(i, end=', ')
            par += i
    print()
    print(f'O valor total dos números pares é: {par}')


# Main
somar_par(sortear())
