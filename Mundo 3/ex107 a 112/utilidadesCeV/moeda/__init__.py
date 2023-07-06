def aumentar(n, mais, forma=True):
    valor = n + (n*(mais/100))
    if forma == True:
        return valorMoeda(valor)
    else:
        return valor

def dimunir(n, menos, forma=True):
    valor = n - (n * (menos/100))
    if forma == True:
        return valorMoeda(valor)
    else:
        return valor

def dobro(n, forma=True):
    valor = n*2
    if forma == True:
        return valorMoeda(valor)
    else:
        return valor

def metade(n, forma=True):
    valor = n/2
    if forma == True:
        return valorMoeda(valor)
    else:
        return valor

def valorMoeda(n):
    valor_formatado = f'R${n:.2f}'
    return valor_formatado

def título(msg):
    tam = len(msg)+6
    print('-' * tam)
    print(f'   {msg}')
    print('-' * tam)

def resumo(p, aumento, reducao):
    título('RESUMO DO VALOR')
    print(f'Valor Analisado: {valorMoeda(p)}')
    print(f'Dobro do preço: {dobro(p)}')
    print(f'Metade do preço: {metade(p)}')
    print(f'80% de aumento: {aumentar(p, aumento, True)}')
    print(f'35% de redução: {dimunir(p, reducao, True)}')
    print('-'* 25)