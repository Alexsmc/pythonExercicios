def linha(qnt):
    print('~'*qnt)


def escreva(msg):
    linha(len(msg)+2)
    print(f'{msg:^}')
    linha(len(msg)+2)


# Main
escreva(input('Qual o título do programa? '))
