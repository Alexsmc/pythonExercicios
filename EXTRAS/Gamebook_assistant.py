from random import randint
import json

jogador = list()
dados = dict()


while True:
    print('[1] Novo Jogo:')
    print('[2] Continue')
    print('[3] Batalhar')
    print('[4] Adicionar/Remover Item')
    print('[5] Usar Provisão/Poção')
    print('[6] Salvar')
    print('[7] Salvar e Sair')
    opc = int(input("O que deseja? "))
    if opc == 1:
        print('Construindo um novo personagem: ')
        dados['Nome: '] = str(input('Nome: '))
        dados['Habilidade inicial: '] = randint(1,6) + 6
        dados['Energia inicial: '] = randint(2,12) + 12
        dados['Sorte inicial: '] = randint(1,6) + 6
        dados['Ouro: '] = 10
        dados['Joias: '] = 0
        print('Escolha uma poção:')
        print('[1] Poção de Habilidade - Recupera os pontos de HABILIDADE')
        print('[2] Poção de Força - recupera os pondots de ENERGIA')
        print('[3]Poção da Fortuna - Recupera os pontos de Sorte e SORTE +1')
        poc = int(input('Escolha: '))
        if poc == 1:
            dados['Poção: '] = 'Poção de HABILIDADE'
        elif poc == 2:
            dados['Poção: '] = 'Poção de ENERGIA'
        elif poc == 3:
            dados['Poção: '] = 'Poção da FORTUNA'
        dados['Itens: '] = ['Espada','Armadura de Couro']
        dados['Provisões: '] = 10
        jogador.append(dados.copy())
        with open('Gamebook_file.txt', 'w', encoding='utf-8') as arquivo:
            json.dump(jogador, arquivo)
        for e in jogador:
            for k, v in e.items():
                print(f'{k}{v}')
    elif opc == 2:
        with open('Gamebook_file.txt', 'r', encoding='utf-8') as arquivo:
            jogador = json.load(arquivo)
        for e in jogador:
            for k, v in e.items():
                print(f'{k}{v}')
    elif opc ==3:
    elif opc == 7:
        print('Até a proxima')
        with open('Gamebook_file.txt', 'w', encoding='utf-8') as arquivo:
            json.dump(jogador, arquivo)
        break