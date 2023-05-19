listagem = ('pão', 1, 'Leite', 2)
print('-'*40)
print(f'{"LISTA DE ITENS":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos%2 ==0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)
'''
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')
print('Comi pra caramba')
'''