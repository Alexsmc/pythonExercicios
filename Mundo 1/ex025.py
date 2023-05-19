print('''crie um programa que  leia o nome de uma pessoa
e diga e tem 'SILVA' no nome''')

nome = str(input('Qual seu nome? ')).strip()
print('seu nome tem Silva? {}'.format('SILVA' in nome.upper()))