def separa(a):
    pares = []
    impares = []
    for i in range(len(a)):
        if ((a[i] % 2) == 0):
            pares.append(a[i])
        else:
            impares.append(a[i])

    return pares, impares

def saida(nomeLista, lista):
    print(f"{nomeLista} = [", end="")
    for i in range(len(lista)):
        print(f"{lista[i]}", end="")
        if (i != (len(lista)-1)): # não é o último elemento
            print(end=", ")
    print("]")

# módulo principal
x = [7, 1, 4, 3, 7, 8, 10, 2, 11]

a, b = separa(x)

saida("original", x)
saida("pares...", a)
saida("ímpares.", b)