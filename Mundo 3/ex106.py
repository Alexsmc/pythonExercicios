C = ('\033[m',          #0 - Sem cores
     '\033[0;30;41m',   #1 - Vermelho
     '\033[0;30;42m',   #2 - Verde
     '\033[0;30;43m',   #3 - Amarelo
     '\033[0;30;44m',   #4 - Azul
     '\033[0;30;45m',   #5 - Roxo
     '\033[7;30m',      #6 - Branco
     )

def interactive_help(fun_or_lib):
    título(f'Acessando o manual do comando \'{fun_or_lib}\'', 4)
    print(C[6], end='')
    help(fun_or_lib)
    print(C[0], end='')

def título(msg, cor=0):
    tam = len(msg)+4
    print(C[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(C[0], end='')

# Main
while True:
    título('SISTEMA DE AJUDA PYHELP', 2)
    resp = input('Função ou Biblioteca > [FIM para sair] ').strip()
    if resp.upper() == 'FIM':
        título('ATÉ LOGO!', 1)
        break
    else:
        interactive_help(resp)