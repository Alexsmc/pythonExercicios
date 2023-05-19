import random
print(" Jogo de advinhacao: \nAcerte o numero q estou pensando")
#chute = random.randint(0,100)#(input(" Qual seu palpite? "))
chutemin = int(0)
chutemax = int(100)
lc = random.randint(chutemin,chutemax)
chute = random.randint(0, 100)
tnt = int(0)
print(chute)
while chute!=lc:
    print(" numero errado. tente de novo.")
    if(chute!=lc):
        if (chute > lc):
            print(" Chute menos")
            chutemax = int(chute - 1)
            chute = random.randint(chutemin, chutemax)
            print(chute)
            tnt = tnt +1
        else:
            print(" Chute mais")
            chutemin = int(chute + 1)
            chute = random.randint(chutemin, chutemax)
            print(chute)
            tnt = tnt + 1

total = 100-tnt
print(" Parabens voce acertou")
print (' o numero é', lc)
print (' vc tentou', tnt, 'vezes')
print(" pontuação: ",total)
