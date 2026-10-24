# arquivo de módulos (ou biblioteca de funções) com 3 funções:
# 1) mostrar_numeros(n) - mostra os números de 1 a n
# 2) somar_numeros(n) - soma os números de 1 a n
# 3) resultados(n) - mostra os números de 1 a n e a soma

def mostrar_numeros(n):
    print("{", end="")
    for i in range(1, n+1):
        print(f"{i}", end="")
        if (i != n): # não é o último elemento
            print(end=", ")
    print("}")

def somar_numeros(n):
    # soma os números de 1 a n
    soma = 0
    for i in range(1, n+1):
        soma = soma + i
    return(soma)

def resultados(n):
    mostrar_numeros(n)
    print(f"Soma: {somar_numeros(n)}")
    print()