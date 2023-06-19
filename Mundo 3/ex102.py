def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = n
    for c in range(n-1, 0, -1):
        f *= c
    if show:
        for c in range(n, 0, -1):
            print(f'{c}', end=" X ")
        print(f' = {f}')
    else:
        print(f'O valor fatorial é: {f}')


# Main
fatorial(int(input('Qual número deseja ver o fatorial? ')),True)