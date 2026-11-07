from Ponto import Ponto
import sys
sys.path.append("C:\Python_IAGA\Python\Avançado")
from Geral import cls

cls()
n = int(input("Digite a quantidade de pontos: "))

# declarando uma coleção de objetos do tipo Ponto
pontos = []
for i in range(n):
    print()
    print(f"Digite as coordenadas do ponto {i + 1}:")
    x = int(input("Digite o valor da coordenada 'x': "))
    y = int(input("Digite o valor da coordenada 'y': "))

    p = Ponto(x, y)  # criando um objeto do tipo Ponto
    pontos.append(p)  # adicionando o objeto criado na coleção

print()
for i in range(n):
    print(f"{i+1}o. ponto: {pontos[i]}")  # chamando o método __str__() do objeto