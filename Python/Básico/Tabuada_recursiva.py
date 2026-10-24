# recursividade = recorrência, módulo que no seu
# corpo tem uma chamada a si próprio

# módulo "tabuada" recursivo
def tabuada(n, i):
    if i <= 10:
        print(f"{n} x {i} = {n * i}")
        i = i + 1
        tabuada(n, i) # recursividade, chamada a si próprio
    else:
        print()

# módulo principal (main)
tabuada(5, 1) # aqui é a primeira chamada da função "tabuada"