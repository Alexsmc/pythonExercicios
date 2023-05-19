# Crie um conversos de moeda
# considere dolar RS 3,27

rs = float(input('Digite quanto você tem em Reais: R$ '))
ct = float(input('Digite a cotação atual do dollar: R$ '))
dl = float(rs / ct)
print('Você tem R$ {:2f}, na carteira.'.format(rs))
print('Isso equivale a U$$ {:.2f}'.format(dl))
print('\nCotação atual: US$ {:.2f}'.format(ct))
