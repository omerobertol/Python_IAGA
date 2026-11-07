def sinal_I(n):
    if n < 0:
        return "negativo"

    if n == 0:
        return "neutro"

    if n > 0:
        return "positivo"

def sinal_II(n):
    if n < 0:
        return "negativo"
    else:
        if n == 0:
            return "neutro"
        else:
            return "positivo"
        
def sinal_III(n):
    if n < 0:
        return "negativo"
    elif n == 0:
        return "neutro"
    else:
        return "positivo"

# módulo principal (main)
tam = int(input("Digite o tamanho da entrada: "))

for i in range(1, tam+1):
    print()

    n = int(input(f"Digite o {i}º número: "))
    print(sinal_I(n))
    print(sinal_II(n))
    print(sinal_III(n))