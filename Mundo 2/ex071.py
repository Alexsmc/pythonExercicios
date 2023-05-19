print('{:^30}'.format('BANCO ALEX'))
print('-'*30)
valor = int(input('Qual valor você quer sacar? R$ '))
total = valor
ced = 100
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédula de R${ced}')
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0

    if valor == 0:
        break
print('VOLTE SEMPRE!!!')


