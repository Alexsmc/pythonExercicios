def leiaint(msg):
    valor = 0
    ok = True

    try:
        while ok:
            entrada = str(input(msg))
            if entrada.isnumeric():
                valor = int(entrada)
                ok = False
            else:
                print(f'\033[0;31mERRO! Digite um numero inteiro válido.\033[m')
    except KeyboardInterrupt:
        print('O usuário preferiu não digitar esse número')
    except Exception as erro:
        print(f"Não foi possível executar o programa pelo seguinte erro: {erro.__cause__}")
    else:
        return valor


def leiafloat(msg):
    valor = float(0)
    ok = True
    try:
        while ok:
            entrada = str(input(msg)).strip().replace(',','.')
            if entrada.isalpha() or entrada == '':
                print(f'\033[0;31mERRO! Digite um numero real válido.\033[m')
            else:
                valor = float(entrada)
                ok = False
    except TypeError:
        print('Usuário não digitou um valor válido.')
    except KeyboardInterrupt:
        print('Usuário praferiu não informar o dado.')
    except Exception as erro:
        print(f'Programa não funcionou devido ao seguinte erro: {erro.__cause__}')
    else:
        return valor
