'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
pontuacao = 0
while True:
    computador = randint(0,10)
    num = int(input('Digite um valor: '))
    soma = num + computador
    jogada = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    while jogada not in 'PI':
        jogada = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    if jogada == 'P':
        if (soma % 2) == 0:
            print(f'Você jogou {num} e o computador {computador}.\nTotal de {soma} DEU PAR')
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            print('=-'*20)
            pontuacao +=1
        else:
            print(f'Você jogou {num} e o computador {computador}.\nTotal de {soma} DEU ÍMPAR')
            print('VOCÊ PERDEU')
            break
    else:
        if (soma % 2) == 1:
            print(f'Você jogou {num} e o computador {computador}.\nTotal de {soma} DEU ÍMPAR')
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 20)
            pontuacao += 1
        else:
            print(f'Você jogou {num} e o computador {computador}.\nTotal de {soma} DEU PAR')
            print('VOCE PERDEU!')
            break
print('-='*20)
print(f'GAME OVER! Você venceu {pontuacao} vezes.')