from lib import interface, arquivo

arq = 'lista_de_nomes.txt'

if arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado')
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Ver pessoa cadastrada', 'Cadastrar nova pessoa', 'Sair'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        interface.cabeçalho('Pessoas cadastradas')
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = interface.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        interface.cabeçalho('Até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida\033[m')
