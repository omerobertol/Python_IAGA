x = [10, 2, 7, 8, 5, 3, 22, 17, 18]

# item é o valor que o usuário deseja procurar na lista x
item = int(input())

n = len(x)
achou = False # variável do tipo flag (bandeira)
posAchou = -1

print("{", end="")
for i in range(n):
    print(f"{i}:{x[i]}", end="")
    if (i != n - 1): # não é o último elemento da lista
        print(", ", end="")

    if x[i] == item:
        posAchou = i
        achou = True

print("}")
print()
if achou:
    print(f"Item: {item}, foi encontrado na posicao {posAchou}.")
else:
    print(f"Item: {item}, \"nao\" foi encontrado.")