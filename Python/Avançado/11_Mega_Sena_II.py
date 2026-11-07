from random import choice
from Vetor import saida

while True:
    n = int(input("Quantidade de cartões (no máximo 10, -1 para encerrar): "))
    if n == -1:
        break

    if n < 1 or n > 10:
        print(f"{n}, quantidade inválida! Digite um valor entre 1 e 10.\n")
        continue

    print()
    todos = [i for i in range(1, 61)] # lista com os números de 1 a 60
    for i in range(n):
        jogo = []
        for j in range(6):
            nro = choice(todos) # escolhe um número aleatório da lista
            jogo.append(nro)
            todos.remove(nro) # remove o número escolhido da lista

        print(saida(f"{i+1}o. cartão:", sorted(jogo)))

    print()