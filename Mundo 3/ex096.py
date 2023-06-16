def área(largura, cumprimento):
    area = largura * cumprimento
    print(f'Largura: {largura}m\nCumprimento: {cumprimento}m')
    print(f'O valor da área do terreno é: {area}m²')

def linha():
    print('-'*30)


#programa principal
print('   Controle de terrenos')
linha()
ladoA = int(input('LARGURA (m): '))
ladoB = int(input('CUMPRIMENTO (m): '))
área(ladoA, ladoB)