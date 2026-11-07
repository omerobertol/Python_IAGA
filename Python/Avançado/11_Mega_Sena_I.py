from random import randint
from Vetor import saida

while True:
    n = int(input("Quantidade de cartões (no máximo 10, -1 para encerrar): "))
    if n == -1:
        break

    if n < 1 or n > 10:
        print(f"{n}, quantidade inválida! Digite um valor entre 1 e 10.\n")
        continue

    print()
    todos_Os_Jogos = []
    for i in range(n):
        jogo = []

        j = 1 # variável de controle do while
        while j <= 6:
            nro = randint(1, 60)
            if nro not in todos_Os_Jogos:
                jogo.append(nro)
                todos_Os_Jogos.append(nro)
                j = j + 1 # passo da variável de controle

        print(saida(f"{i+1}o. cartão:", sorted(jogo)))

    print()