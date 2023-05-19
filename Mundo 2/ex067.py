calculo = 0
while True:
    num = int(input('Quer a tabuada de qual valor? '))
    if num < 0:
        break
    for i in range(1, 11):
        calculo = num * i
        print(f'{num} x {i:2} = {calculo}')
    print('-'*20)
print('Obrigado por usar o programa!!')