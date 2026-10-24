# "math" é uma biblioteca que contém funções matemáticas, 
# como a função sqrt() que calcula a raiz quadrada de 
# um número.
from math import sqrt

# Entrada de Dados
n = int(input("Digite um número: "))

# Processamento: Operações Matemáticas
dobro = n * 2
triplo = n * 3
quadrado = n ** 2
cubo = n ** 3
raizQuadrada = sqrt(n)

# Saída de Dados
print()
print(f"Sendo n = {n}, temos:")
print(f"Dobro = {dobro}")
print(f"Triplo = {triplo}")
print(f"Quadrado = {quadrado}")
print(f"Cubo = {cubo}")
print(f"Raiz Quadrada = {raizQuadrada:.4f}")