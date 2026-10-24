# Subprograma (pedaço de código) = função = módulo
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

# módulo principal (main)
resultados(7)
resultados(10)

# Estrutura modularizada baseada em 4 módulos (funções)
# 1) mostrar_numeros(n) - mostra os números de 1 a n
# 2) somar_numeros(n) - soma os números de 1 a n
# 3) resultados(n) - mostra os números de 1 a n e a soma
# 4) módulo principal (main) - chama a função resultados(n) para n = 7 e n = 10