import nt


def ficha(nome='<desconhecido>', gol=0):
    """
    -> Função mostra o nome e o numero de gols do jogador cadastrado.
    :param nome: recebe um nome
    :param gol: recebe o numero de gols
    :return: mostra o nome e o numero de gols na tela
    """
    print(f'O jogador {nome} fez gol(s) {gol} no campeonato.')


# Main
nome = str(input('Nome do Jogador: '))
gol = str(input('número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gol)
else:
    ficha(nome, gol)
