'''
Crie um programa que faça o programa jogar Jokenpô
'''
'''
from random import randint
print('-='*5)
print('  JOKEPÔ')
print('-=' *5)

escolha = int(1)
maquina = int(0)
player = int(0)

while escolha != 0:
    emaquina = randint(1,3)
    print('Escolha sua arma')
    print('\nJogador {} x {} Maquina\n'.format(player,maquina))
    print('[1]Pedra')
    print('[2]Papel')
    print('[3]Tesoura')
    print('[0]Sair')
    escolha = int(input('Faça sua escolha: \n'))
    if (escolha == 1) and (emaquina == 2):
        print('Você deu PEDRA e a máquina PAPEL')
        print('Vitória da MAQUINA')
        maquina = maquina + 1
    elif (escolha == 1) and (emaquina==3):
        print('Você deu PEDRA e a máquina TESOURA')
        print('Vitória do JOGADOR')
        player = player + 1
    elif (escolha == 2) and (emaquina == 1):
        print('Você escolheu PAPEL e a máquina PEDRA')
        print('Vitória do JOGADOR')
        player = player + 1
    elif (escolha == 2) and (emaquina == 3):
        print('Você escolheu PAPEL e a maquina TESOURA')
        print('Vitória da MAQUINA')
        maquina = maquina + 1
    elif (escolha == 3) and (emaquina == 1):
        print('Você escolheu TESOURA e a maquina PEDRA')
        print('Vitória da MAQUINA')
        maquina = maquina +1
    elif (escolha == 3) and (emaquina == 2):
        print('Você escolheu TESOURA e a máquina PAPEL')
        print('Vitória do JOGADOR')
        player = player +1
    elif (escolha == emaquina):
        print('EMPATE')
    elif (escolha>3) or (escolha<0):
        print('OPÇÃO INVÁLIDA\n')
'''
#Programa desenvolvido por Alex Martins

from random import randint
from time import sleep
itens = (' ','PEDRA', 'PAPEL', 'TESOURA')
jogador = int(1)
placar_jogador = int(0)
placar_computador = int(0)
while jogador !=0:
    computador = randint(1,3)
    print('''Suas Opções
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    [0] SAIR
    
    JOGADOR {} X {} COMPUTADOR\n'''.format(placar_jogador,placar_computador))
    jogador = int(input('Qual sua Jogada? '))
    if (jogador>0) and (jogador <=3):
        print('JO')
        sleep(0.8)
        print('KEN')
        sleep(0.8)
        print('PO!!')
        sleep(0.5)
        print('-='*10)
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('-='*10)

        if computador == 1: #pedra
            if jogador == 1:
                print('EMPATE')
            elif jogador == 2:
                print('JOGADOR VENCE')
                placar_jogador = placar_jogador+1
            elif jogador == 3:
                print('COMPUTADOR VENCE!')
                placar_computador = placar_computador + 1
        if computador == 2: #PAPEL
            if jogador == 1:
                print('COMPUTADOR VENCE')
                placar_computador = placar_computador + 1
            elif jogador == 2:
                print('EMPATE')
            elif jogador == 3:
                print('JOGADOR VENCE')
                placar_jogador = placar_jogador + 1
        if computador == 3: #TESOURA
            if jogador == 1:
                print('JOGADOR VENCE')
                placar_jogador = placar_jogador + 1
            elif jogador == 2:
                print('COMPUTADOR VENCE')
                placar_computador = placar_computador + 1
            elif jogador == 3:
                print('EMPATE')
    elif jogador == 0:
        if placar_computador > jogador:
            print('FOI BOM HUMILHAR VOCÊ!!')
        elif placar_jogador > placar_computador:
            print('NA PROXIMA NÃO HAVERÁ MISERICÓRDIA')
        else:
            print('FOI UM DUELO INCRÍVEL')
    else:
        print('JOGADA INVÁLIDA')
