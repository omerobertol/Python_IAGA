import sys
sys.path.append("C:\Python_IAGA\Python\Avançado")
from Geral import parada, cls
import Vetor

def entrada_de_dados(id, tam):
    cls()
    print("***** ENTRADA DE DADOS *****")
    a = Vetor.entrada(id, tam)
    parada()
    return a

def mostrar_itens(id, a):
    cls()
    print("***** MOSTRAR ITENS *****")
    print(Vetor.saida(id, a))
    parada()

def soma_media(id, a):
    cls()
    print("***** SOMA E MÉDIA *****")
    print(Vetor.toString(id, a))
    parada()

def maior_menor(id, a):
    cls()
    print("***** MAIOR E MENOR *****")
    print(Vetor.saida(id, a))
    print()
    print(f"Maior Valor = {Vetor.maior_Valor(a)}")
    print(f"Menor Valor = {Vetor.menor_Valor(a)}")

    parada()