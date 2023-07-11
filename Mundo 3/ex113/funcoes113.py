def leiaint(msg):
    valor = 0
    ok = True

    try:
        while ok:
            entrada = str(input(msg)).strip()
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
            entrada = str(input(msg)).strip().replace(',', '.')
            if entrada.isalpha() or entrada == '':
                print(f'\033[0;31mERRO! Digite um numero real válido.\033[m')
            else:
                valor = float(entrada)
                ok = False
    except (TypeError, ValueError):
        print('Usuário não digitou um valor válido.')
    except KeyboardInterrupt:
        print('Usuário praferiu não informar o dado.')
    except Exception as erro:
        print(f'Programa não funcionou devido ao seguinte erro: {erro.__class__}')
    else:
        return valor

# -------------------------------------------------------------------------------------------


def leiaInt2(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[ERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('n\033[31mUsiário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def leaiafloat2(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[ERRO: por favor digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('n\033[31mUsiário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

