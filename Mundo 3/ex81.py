valores = []
while True
    valores.append(int(input('Digite um valor')))
    r = 'y'
    if r not in 'nN':
        r = input('Quer continuar? [S/N]').strip().upper()

