n1 = int(input('Digite um numero:'))
n2 = int(input('Outro Numero: '))
n3 = int(input('Mais um numero: '))
n4 = int(input('Ultimo número: '))
nums = n1, n2, n3, n4
'''tot9 = 0
totpar = 0
for c in range(0, len(nums)):
    if nums[c]==9:
        tot9 +=1
    if nums[c]%2 == 0:
        totpar += 1'''
print(f'O valor 9 apareceu {nums.count(9)} vezes.')
if 3 in nums:
    print('O valor 3 apareceu na {}ª posição.'.format(nums.index(3)+1))
else:
    print('O Valor 3 não foi digitado em nehuma posição')
print(f'Os valores pares digitados foram: ', end='')
for n in nums:
    if n%2 == 0:
        print(n, end=' ')
