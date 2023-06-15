import datetime
trabalhador = list()
dados = dict()
while True:
    dados['Nome: '] = str(input('Nome: ')).strip().title()
    idade = int(input("Ano de nascimento: "))
    dados['Idade: '] = datetime.date.today().year - idade
    dados['CTPS: '] = int(input('Carteira de Trabalho: (0 não tem): '))
    if dados['CTPS: '] == 0:
        trabalhador.append(dados.copy())
        break
    dados['Ano contratação: '] = int(input('Ano de Contratação: '))
    dados['Salário: R$ '] = float(input('Salário: R$'))
    dados['Aposentadoria com: '] = str(f'{dados["Idade: "]+35} anos.')
    trabalhador.append(dados.copy())
    break

for e in trabalhador:
    for k, v in e.items():
        print(f'{k}{v}')
