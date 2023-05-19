'''
Deizer se um triangluo pe posível ou não a partir de 3 seguimentos dados
dizer que tipo de triangulo é:
- Equilátero: todos o lados iguais
- Isóceles: dois lasdos iguais
- Escaleno: todos lados diferentes
'''

r1 = int(input('Qual valor da reta 1: '))
r2 = int(input('Qual valor da reta 2: '))
r3 = int(input('Qual valor da reta 3: '))

def e_triangulo(la,lb,lc):
    a = float(la)
    b = float(lb)
    c = float(lc)
    if (a+b>c) and (a+c>b) and (b+c>a):
        return True
    else:
        return False

if e_triangulo(r1,r2,r3) == False:
    print('O trinangulo não é possível!')
else:
    print('O trinangulo é possível!', end='')
    if r1 == r2 == r3:
        print('Triangulo EQUILÁTERO')
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print('Triangulo ISÓCELISS')
    else:
        print('Triangulo ESCALENO')


