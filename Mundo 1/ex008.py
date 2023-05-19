# Desafio 8, Escreva um programa que receba
# em metros e converta pra centimetros e milimetros

m = float(input('Digite um valor'))
km = m / 1000
hm = m / 100
dam =m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{}m correpondem a;\n{}Km\n{}hm\n{}dam\n{}dm\n{}Cm\n{}mm'.format(m, km, hm, dam, dm, cm, mm))
