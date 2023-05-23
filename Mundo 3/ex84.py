pessoas = list()
dados = []
mai = men = 0
while True:
    dados.append(str(input('Nome: ')).strip().capitalize())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()
    while resposta not in 'sSnN':
        resposta = str(input('Quer continuar?[S/N]')).strip().upper()
    if resposta in 'nN':
        break

print(f'Foram digitados o total de {len(pessoas)} pessoas')
print(f'O maior peso foi de {mai:.2f}kg:', end=' ')
for p in pessoas:
    if p[1] == mai:
        print(p[0], end=' ')
print(f'O menos peso foi de {men:.2f}kg:', end=' ')
for p in pessoas:
    if p[1] == men:
        print(p[0], end=' ')