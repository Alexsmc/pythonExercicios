expr = str(input('Digite uma Expressão: '))
pilha = []
for simb in expr:
    if simb== '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão esta válida')
else:
    print('Sua Expresão está errada!')
