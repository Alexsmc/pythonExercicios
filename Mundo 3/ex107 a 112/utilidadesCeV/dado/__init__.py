def leiaInt(msg):
    '''
    Função para validar se o dado é um numero inteiro
    :param n: pega o numero digitado pelo usuário
    :return: retona o numero se verdadeiro
    '''

    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
        if ok:
            break
    return valor


def leiaFloat(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)
