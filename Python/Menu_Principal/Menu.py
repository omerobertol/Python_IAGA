import sys
sys.path.append("C:\Python_IAGA\Python\Avançado")
from Geral import parada, cls
import Opcoes_Menu

a = [] # vetor vazio para armazenar os valores digitados

while True:
    cls()

    print("***** MENU PRINCIPAL *****")
    print("[1] Entrada de Dados")
    print("[2] Mostrar Itens")
    print("[3] Soma e Média")
    print("[4] Maior e Menor")
    print("[9] Sair")

    print()
    opc = int(input("Opção desejada: "))

    if (opc == 1):
        a = Opcoes_Menu.entrada_de_dados("Vetor A", 10)
    elif (opc == 2):
        Opcoes_Menu.mostrar_itens("Vetor A", a)
    elif (opc == 3):
        Opcoes_Menu.soma_media("Vetor A", a)
    elif (opc == 4):
        Opcoes_Menu.maior_menor("Vetor A", a)
    elif (opc == 9):
        break
    else:
        print(f"{opc}, opção inválida! Tente novamente.")
        parada()

    