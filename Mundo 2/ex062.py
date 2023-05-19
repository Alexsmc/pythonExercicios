termo = int(input('Digite o PRIMEIRO TERMO'))
razao = int(input('Em qual RAZÃO?'))
termomax = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while termomax <= total:
        print(termo, end=' -> ')
        termo += razao
        termomax += 1
    print("PAUSA")
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados'.format(total))
