def calc_idade(ano_nasc):
    """
    Função que calcula a idade atual do individuo
    :param ano_nasc: recebe o ano que o usuário nasceu
    :return: retorna a idade atual do usuário
    """
    import datetime
    idade = datetime.date.today().year - ano_nasc
    return idade


def voto(idade):
    if idade < 16:
        print(f'com {idade} anos: VOTO NEGADO')
    elif 18 <= idade <= 64:
        print(f'com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        print(f'com {idade} ano: VOTO OPCIONAL')


# Programa Principal
idade_atual = calc_idade(int(input('Em que ano você nasceu? ')))
voto(idade_atual)
