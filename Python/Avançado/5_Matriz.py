def linha(n):
    print(" "*9, "+", ("-" * 3) * n, "-+", sep="")

def matriz_I(n): # n é o tamanho da matriz quadrada
    linha(n) # borda superior da matriz
    i = 0 # variável de controle do laço de repetição
    while i < n:
        print(f"linha {i}: | ", end="")
        j = 0 # variável de controle do laço de repetição
        while j < n:
            print(f"{i}{j}", end=" ")
            j = j + 1 # incremento da variável de controle do laço de repetição

        print("|") # quebra de linha
        i = i + 1 # incremento da variável de controle do laço de repetição
    linha(n) # borda inferior da matriz

def matriz_II(n): # n é o tamanho da matriz quadrada
    linha(n) # borda superior da matriz
    for i in range(n):
        print(f"linha {i}: | ", end="")
        for j in range(n):
            print(f"{i}{j}", end=" ")
        print("|") # quebra de linha
    linha(n) # borda inferior da matriz
    
# módulo principal (main)
n = int(input("Digite o tamanho da matriz quadrada: "))
print()

matriz_I(n) # na versão com while, a matriz é impressa de 0 até n-1
print()
matriz_II(n) # na versão com for, a matriz é impressa de 0 até n-1