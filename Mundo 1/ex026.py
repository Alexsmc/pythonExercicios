print('''Faça um programa que leia uma frse pelo teclado e mostre:
- Quantas vezes a parace a letra 'A'
- Em que posição ela aparece pela primeira vez.
- Em que posição ela aprecepela ultima vez''')

frase = str(input("Digite sua frase: ")).strip().upper()
print('A letra "A" aparece {} vezes na frase:  '.format(frase.count('A')))
print('A letra "A" primeiro no posição {}. '.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição: {}'.format(frase.rfind('A')+1))
