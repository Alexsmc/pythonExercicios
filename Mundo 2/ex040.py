'''
média menor q 5 reprovado
entre 5 e 6.9 em recuperação
maior q 7 ou mais aprovado
'''

nota1 = float(input('Gigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1+nota2)/2

if media >= 7:
    print('APROVADO')
    print('Media {:.1f}'.format(media))
elif 7 > media >= 5:
    print('Em recuperação')
    print('Média {:.1f}'.format(media))
else:
    print('REPROVADO')
    print('média {:.1f}'.format(media))
