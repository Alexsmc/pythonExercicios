valores = []
while True:
    valores.append(int(input('Digite um valor')))
    r = 'z'
    while r not in 'sSnN':
        r = input('Quer continuar? [S/N]').strip().upper()
    if r in 'nN':
        break
print(f'Você digitou {len(valores)} Elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O Número 5 está na lista')
else:
    print('Você não digitou o N° 5')
