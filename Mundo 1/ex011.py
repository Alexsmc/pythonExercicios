# Faça um programa que leia a altura e largura de uma parede
# em mestros. Calcule a quantidade de tinta necessária pra pinta-la
# sabendo que cada litro de tinta pinta uma área de 2m².

h = float(input('Qual altura da marede em metros? '))
b = float(input('Qual largura da parede em metros? '))
a = float(b*h)
l = float(a/2)
print("Para uma parade de {:.2f}m², será necessário {:.2f}l de tinta.".format(a, l))
