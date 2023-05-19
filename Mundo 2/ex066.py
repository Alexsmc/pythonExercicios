cont = soma = 0
while True:
    num = int(input('Digite um numero: [999 para sair]'))
    if num == 999:
        break
    cont += 1
    soma += num

print(f'Você digitou {cont} números')
print(f'A soma deles é igual a {soma}')