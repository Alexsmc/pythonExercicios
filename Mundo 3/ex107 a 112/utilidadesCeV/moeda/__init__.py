def aumentar(n, taxa, formato=True):
    valor = n + (n * (taxa / 100))
    if formato:
        return valorMoeda(valor)
    else:
        return valor


def dimunir(n, taxa, formato=True):
    valor = n - (n * (taxa / 100))
    if formato:
        return valorMoeda(valor)
    else:
        return valor


def dobro(n, format=True):
    valor = n*2
    if format:
        return valorMoeda(valor)
    else:
        return valor


def metade(n, formato=True):
    valor = n/2
    if formato:
        return valorMoeda(valor)
    else:
        return valor


def valorMoeda(n = 0, moeda = 'R$'):
    valor_formatado = f'{moeda}{n:>.2f}'.replace('.',',')
    return valor_formatado


def titulo(msg):
    tam = len(msg)+14
    print('-' * tam)
    print(f'{msg}'.center(tam))
    print('-' * tam)


def resumo(p, aumento, reducao):
    titulo('RESUMO DO VALOR')
    print(f'Valor Analisado: \t{valorMoeda(p):>}')
    print(f'Dobro do preço: \t{dobro(p):>}')
    print(f'Metade do preço: \t{metade(p):>}')
    print(f'{aumento}% de aumento: \t{aumentar(p, aumento, True):>}')
    print(f'{reducao}% de redução: \t{dimunir(p, reducao, True):>}')
    print('-'* 27)
