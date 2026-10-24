def menor(a, b):
    if a < b:
        return a
    else:
        return b

def maior(a, b):
    if a > b:
        return a
    else:
        return b

def menor_maior(a, b):
    if a < b:
        return(a, b)
    else:
        return b, a

def mostrar(a, b):
    print(f"Menor: {a}")
    print(f"Maior: {b}")

# módulo principal (main)
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número.: "))

menor_valor = menor(a, b)
maior_valor = maior(a, b)

print()
mostrar(menor_valor, maior_valor)

print()
menor_valor, maior_valor = menor_maior(a, b)
mostrar(menor_valor, maior_valor)