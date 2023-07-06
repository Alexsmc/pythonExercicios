def aumentar(n, forma=True):
    valor = n + (n*(10/100))
    if forma == True:
        return valorMoeda(n)
    else:
        return valor

def dimunir(n, forma=True):
    valor = n - (n * (13/100))
    if forma == True:
        return valorMoeda(n)
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
    valor_formatado = f'R$ {n:.2f}'
    return valor_formatado