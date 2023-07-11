from lib import interface

while True:
    resposta = interface.menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        interface.cabeçalho('opc 1')
    elif resposta == 2:
        interface.cabeçalho('opc 2')
    elif resposta == 3:
        interface.cabeçalho('Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida\033[m')
