from os import system
from time import sleep

def cls():
    system("cls")

def delay(tmp): # tmp em segundos
    sleep(tmp)

def parada():
    print("\nPressione <Enter> para prosseguir...")
    input()

def confirmou(rotulo):
    op = input(rotulo)
    if ((op == "s") or (op == "S")):
        return True
    else:
        return False
    
def linha(tipo="-", tam=20):
    result = ""
    for i in range(tam):
        result += tipo

    return result

