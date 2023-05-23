matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior2l = totalpar = totalcol3 = 0
for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
print('='*20)
for l in range(3):
    for c in range(3):
        if matriz[l][c]%2 == 0:
            totalpar += matriz[l][c]
        print(f'[{matriz[l][c]:^3}]', end='')
    print()
for l in range(3):
    totalcol3 += matriz[l][2]
for c in range(3):
    if matriz[1][c] > maior2l:
        maior2l = matriz[1][c]

print(f'A soma de todos os valores pares é: {totalpar}')
print(f'A soma dos valores da 3º coluna é: {totalcol3}')
print(f'O maior valor da segunda linha é: {maior2l}')
