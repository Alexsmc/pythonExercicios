jogador = {}
partidas = []
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(total):
    partidas.append(int(input(f'  Quantos gols na {c+1}º partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na pratida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')


'''dados['Nome: '] = str(input('Nome do Jogador: ')).strip().title()
partidas = int(input('Quantas partidas ele jogou? '))
for i in range(partidas):
    pontuação = int(input(f'Quantos Gols na partida {i+1}? '))
    gol.append(pontuação)
    dados['gols'] = gol
    total += pontuação
    dados['total: '] = total
jogador.append(dados.copy())
print(jogador)
print('=-'*30)
for e in jogador:
    for k, v in e.items():
        print(f'O campo {k} tem Valor: {v}')
print('-='*30)
print(f'O jogador {jogador["Nome: "]} jogou {partidas} partidas.')
for i, a in enumerate(gol):
    print(f'=> NA partida, {i+1}, fez {a} gols')
print(f'fez um total de {jogador[2]}')'''
