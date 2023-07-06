import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.valorMoeda(p)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.valorMoeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, True)}')
print(f'Reduzindo 13%, tmeos {moeda.dimunir(p, True)}')
