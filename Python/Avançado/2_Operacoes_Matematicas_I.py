# "math" é uma biblioteca que contém funções matemáticas, 
# como a função sqrt() que calcula a raiz quadrada de 
# um número.
from math import sqrt

# Processamento: Operações Matemáticas
def dobro(n):
    return n * 2

def triplo(n):
    return n * 3

def quadrado(n):
    return n ** 2

def cubo(n):
    return n ** 3

def raizQuadrada(n):
    return sqrt(n)

def toString(n):
    result = f"______Sendo n = {n}, temos:\n"
    result += f"Dobro         = {dobro(n)}\n"
    result += f"Triplo        = {triplo(n)}\n"
    result += f"Quadrado      = {quadrado(n)}\n"
    result += f"Cubo          = {cubo(n)}\n"
    result += f"Raiz Quadrada = {raizQuadrada(n):.4f}\n"
    
    return result

# módulo principal (main)
# Entrada de Dados
n = int(input("Digite um número: "))

print()
print(toString(n))