total = barato = mais_mil = cont = 0
produto_barato = ' '
print('-'*30)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-'*30)

while True:
    produto = str(input('Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$ '))
    total += preco
    if preco >= 1000:
        mais_mil += 1
    if cont == 0 or preco <barato:
        barato = preco
        produto_barato = produto
        cont +=1
    continuar = ' '
    while continuar not in 'S/N':
        continuar = str(input('Quer conntinuar? [S/N]? ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total de compra foi: R$ {total:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1.000,00')
print(f'O produto mais barato foi {produto_barato} que custa R$ {barato:.2f}.')