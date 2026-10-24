n = 7

print("{", end="")
for i in range(1, n+1):
    print(f"{i}", end="")
    if (i != n): # não é o último elemento
        print(end=", ")
print("}")

soma = 0
for i in range(1, n+1):
    soma = soma + i
print(f"Soma: {soma}")
print()
# --------------------------------------------------
n = 10

print("{", end="")
for i in range(1, n+1):
    print(f"{i}", end="")
    if (i != n): # não é o último elemento
        print(end=", ")
print("}")

soma = 0
for i in range(1, n+1):
    soma = soma + i
print(f"Soma: {soma}")
print()