valores = list()
for i in range(5):
    n = int(input('Digite um numero: '))
    if i == 0 or n > valores[len(valores)-1]:
        valores.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'adicionado na posição {pos} da lista')
                break
            pos += 1

#valores.sort()
print(f'Os valores digitados em ordem foram: {valores}')