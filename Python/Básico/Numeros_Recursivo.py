# Subprograma (pedaço de código) = função = módulo
def mostrar_numeros(n, i):
    if i <= n:
        if i == 1:
            print("{", end="")

        print(f"{i}", end="")
        if (i != n): # não é o último elemento
           print(end=", ")

        i = i + 1
        mostrar_numeros(n, i) # recursividade, chamada a si próprio
    else:
        print("}")

def somar_numeros(n, i):
    if i <= n:
        novoI = i + 1
        return i + somar_numeros(n, novoI) # recursividade, chamada a si próprio
    else:
        return 0

def resultados(n):
    mostrar_numeros(n, 1)
    print(f"Soma: {somar_numeros(n, 1)}")
    print()   

# módulo principal (main)
resultados(5)