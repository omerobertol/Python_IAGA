s = input("Informe uma String: ")

n = len(s) # tamanho da lista

print()
# matriz de caracteres quadrada n x n
for i in range(n):
    for j in range(n):
        print(s[j], end=" ")
    print()

print("--------------------------------")
# matriz de triangula inferior
for i in range(n):
    for j in range(i + 1):
        print(s[j], end=" ")
    print()
    
print("--------------------------------")
for i in range(n):
    for j in range(i + 1):
        print(s[j], end=" ")

    for j in range(i + 1, n):
        print("*", end=" ")
    print()