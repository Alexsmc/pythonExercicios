valores = []
pares = []
impares = []
while True:
    valores.append((int(input('Digite um Número:'))))
    resp = str(input('Quer continuar? S/N')).strip().upper()
    if resp in 'nN':
        break

for p, v in enumerate(valores):
    if v%2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Você digitou os números: {valores}')
print(f'Destes, são pares os: {pares}')
print(f'Destes, são ímpares os: {impares}')
