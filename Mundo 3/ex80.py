valores = list()
for i in range(5):
    valores.append(int(input('Digite um numero: ')))
    for p, v in enumerate(valores):
        if v == max(valores):
            print('salvo na ultima casa')
        elif v == min(valores):
            print('salvo na primeira posição')
        else:
            print(f'Valor salvo na casa {p}')

#valores.sort()
print(f'Os valores digitados em ordem foram: {valores}')