jogador = list()
dados = dict()
gol = []
total = 0
dados['Nome: '] = str(input('Nome do Jogador: ')).strip().title()
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
print(f'fez um total de {jogador[2]}')