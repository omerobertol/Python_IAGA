n = int(input("Tamanho da lista: "))

print()

soma = 0
l = [] # lista vazia
for i in range(n):
    item = int(input(f"Digite o {i + 1}º elemento da lista: "))

    soma = soma + item
    l.append(item)

print()
# 1a. forma: print da lista toda
print(l, "soma =", soma)

# 2a. forma: print da lista item a item
for item in l: # for each
    print(f"{item}", end=", ")
print("soma =", soma)

# 3a. forma: print da lista item a item com índice
print("[", end="")  
for i in range(n):
    print(f"{l[i]}", end="") 
    if (i != (n-1)): # não é o último elemento
        print(end=", ")
print("] soma =", soma)  
