termo = int(input('Digite o PRIMEIRO TERMO'))
razao = int(input('Em qual RAZÃO?'))
termomax = 1

while termomax <= 10:
    print(termo, end=' -> ')
    termo += razao
    termomax += 1
print("It's over!")