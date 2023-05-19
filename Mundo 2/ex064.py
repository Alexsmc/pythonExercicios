num = digitado = soma = int(0)
while num != 999:
    print('Digite 999 pra sair')
    num = int(input('Digite um numero: '))
    if num != 999:
        digitado += 1
        soma += num
print("Foram Digitados {}, numeros e a soma total deles é: {}".format(digitado,soma))
