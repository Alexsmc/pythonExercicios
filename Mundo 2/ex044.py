'''
Elabrore um programa que calcula uma quantidade de desconto baseado
na forma de pagamanto do cliente

pagamento a visa no dinheiro 10% de desconto
pagamento a vist ano cartão 5% de desocnto
pagamento 2x no cartão preço normal
pagamento 3x ou mais 20% de juros
'''

preco = float(input('Qual o preço? R$ '))
menu = 1

while menu != 0:
    print("Escolha uma opção:")
    print('[1] Pagamento a Vista: 10% de DESCONTO')
    print('[2] pagamento a vista no cartão 5% de DESCONTO')
    print('[3] Pagamento parcelado')
    print('[0] SAIR')
    menu = int(input('Escolha a opção: '))
    if menu == 1:
        print('\nOpção [1] Pagamento a Vista: 10% de DESCONTO')
        npreco = preco - (preco * 10/100)
        print('Valor a ser pago R$ {:.2f}\n'.format(npreco))
    elif menu == 2:
        print('\nOpção [2] pagamento a vista no cartão 5% de DESCONTO ')
        npreco = preco - (preco * 5/100)
        print('O valor a ser pago será de R${:.2f}\n'.format(npreco))
    elif menu == 3:
        print('\n2x no cartão. PREÇO NORMAL')
        print('3x ou mais, juros de 20%')
        parcela = int(input('Quantas parcelas você deseja: '))
        if parcela ==2:
            npreco = float(preco/2)
            print('\nO valor das parcelas será de R${} cada.\n'.format(npreco))
        elif parcela >= 3:
            npreco = float((preco + (preco * 20/100)))
            print('\nJuros de 20% aplicado')
            print('Novo preço será de R${:.2f}\n'.format(npreco))
            npreco = npreco/parcela
            print('E será dividido em {} vezes de R${:.2f}.\n'.format(parcela,npreco))
        else:
            print('\nReveja as opções\n')
    elif (menu < 0) or (menu > 3):
        print('\nOPÇÃO ERRADA\n')
    #elif type(menu) != int:
     #   print('\nOPÇÃO ERRADA\n')