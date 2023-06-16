from time import sleep


def linha():
    print('-='*40)


def maior(* num):
    linha()
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v}', end=', ')
        sleep(0.5)
    print(f'Foram adicionados {len(num)} valores ao todo.')
    print(f'O maior número informado é: {max(num)}')


# Main
maior(5, 2, 1, 9, 45, 101)
maior(4, 5, 45, 1, 0, 100, 200, 15)
maior(0, 1)
maior(5, 6, 7, 78)
