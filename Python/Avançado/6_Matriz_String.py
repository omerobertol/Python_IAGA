def linha(n):
    print(" "*(10+(n // 100)), "+", ("-" * 2) * n, "-+", sep="")

def matriz_String(s): # n é o tamanho da matriz quadrada
    linha(len(s))
    n = len(s) # tamanho da string
    for i in range(n):
        print(f"linha {i:2}: | ", end="")
        # matriz triangular inferior
        for j in range(i+1):
            print(f"{s[j]}", end=" ")
        # matriz triangular superior
        for j in range(i+1, n):
            print("  ", end="")
        print("|") # quebra de linha
    linha(len(s))

# módulo principal (main)
s = input("Informe uma String: ")

print()

matriz_String(s)