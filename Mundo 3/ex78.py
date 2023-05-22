valores = []
for i in range(5):
    valores.append(int(input(f'Digite um valor na posiçao {i}: ')))

print('='*40)
print(f'Você digitou os numeros: {valores}')
print(f'O maior valor foi: {max(valores)} nas posições: ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(f'{p}...', end='')
print(f'\nO menor valor foi {min(valores)} nas posições: ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(f'{p}...', end='')
