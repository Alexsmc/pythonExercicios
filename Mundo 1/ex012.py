# Crie um algoritimo que leia o preço de um produto
# e calcule seu novo preço com 5% de desocnto.

p = float(input('Quanto custa? R$ '))
d = float(input('Qual desconto? %'))
np = float(p-(p*d/100))
print("Desconto de R$ {:.2f}".format(np-p))
print('Novo Preço: R$ {:.2f}'.format(np))
