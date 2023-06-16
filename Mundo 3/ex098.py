from time import sleep
def contador(inicio, fim, passo):
    if passo <0:
        passo *= -1
    elif passo == 0:
        passo = 1

    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=', ')
            inicio += passo
            sleep(0.5)
    elif inicio >= fim:
        while inicio >= fim:
            print(inicio, end=', ')
            inicio -= passo
            sleep(0.5)
    else:
        print('Contagem não possível')
    print('Contagem encerrada')


# Main
i = int(input('Valor inicial da contagem: '))
f = int(input('Valor Final da contagem: '))
p = int(input('Valor do intervalo da contagem: '))
contador(1, 10, 1)
contador(10, 0, 2)
contador(i, f, p)
