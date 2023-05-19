valores = list()
for i in range(5):
    valores.append(int(input(f'Digite um valor na posiçao {i}: ')))

print('='*40)
print(f'Você digitou os numeros: {valores}')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'O valor {v} é o maior e está na posição {p}')
    elif v == min(valores):
        print(f'O valor {v} é o menor e está na posição {p}')
#print(f'O maior valor foi {max(valores)} e está na posição {enumerate(max(valores))}')