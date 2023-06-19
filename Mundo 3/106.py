def interactive_help(fun_or_lib):
    help(fun_or_lib)

while True:
    resp = input('Função ou Biblioteca > [FIM para sair] ').strip()
    if resp.upper() == 'FIM':
        print('Até logo!')
        break
    else:
        interactive_help(resp)