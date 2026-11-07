from Meu_Math import divisores, ehPrimo
from Vetor import saida

while True:
    n = int(input("n (-1 para encerrar): "))
    if n == -1:
        break

    x = divisores(n)
    print(saida(f"Divisores de {n}", x))
    if ehPrimo(n):
        print("<<< número primo >>>")
    print()