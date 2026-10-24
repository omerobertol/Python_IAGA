from random import randint

jogo = [] # lista vazia para armazenar os números sorteados

i = 1 # variável de controle do while
while (i <= 6):
    n = randint(1, 60)
    if (n not in jogo):
        jogo.append(n)
        i = i + 1 # passo da variável de controle

jogo.sort() # coloca os números em ordem crescente

print(jogo)
