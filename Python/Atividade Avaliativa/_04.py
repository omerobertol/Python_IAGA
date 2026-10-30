n = int(input())

for i in range(n):
    for j in range(n):
# i == 0 primeira linha
# i == n - 1 última linha
# j == 0 primeira coluna
# j == n - 1 última coluna
        if (i == 0 or i == n - 1 or j == 0 or j == n - 1):  
            print("* ", end="")
        else: # parte interna da matriz
            print("@ ", end="")

    print()