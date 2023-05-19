maior = menor = digitado = soma = media = int(0)
continuar = 'Y'
while continuar in 'Yy':
    num = int(input('Digite um número: '))
    digitado += 1
    if digitado == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    soma += num
    continuar = str(input('Quer Continuar? [y/n] ')).strip().upper()[0]
    while continuar not in 'yYnN':
        print('opção invalida')
        continuar = str(input('Quer Continuar? [y/n] ')).strip().upper()[0]
media = int(soma / digitado)
print(f"A média dos numeros é: {media}")
print(f'O maior numero é: {maior}')
print(f'O menor numero é: {menor}')
