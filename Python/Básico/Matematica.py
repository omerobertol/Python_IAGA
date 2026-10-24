def soma(a, b):
    return a + b

def mult(a, b):
    return a * b

# módulo principal (main)
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número.: "))

print()
print(f"{a} + {b} = {soma(a, b)}")
print(f"{a} * {b} = {mult(a, b)}")