# Aluguel de carros

cd = int(input('Quantos dias ficou com o carro? '))
km = float(input('Quantos Kilometros foram rodados? '))
vd = float(60)
vk = float(0.15)
to = float((vd*cd)+(km*vk))
print("O valor tatal é: R$ {:.2f}".format(to))
