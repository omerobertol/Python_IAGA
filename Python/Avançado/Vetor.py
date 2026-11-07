def entrada(id, tam):
    x = [] # uma lista vazia equivalente a um array (vetor)
    for i in range(tam):
        vlr = int(input(f"Digite o {i+1}º valor, {id}[{i}]: "))
        x.append(vlr) # adiciona o valor digitado no final da lista

    print()
    return x

def saida(id, x):
    result = f"{id} = ["
    n = len(x)  
    for i in range(n):
        result += f"{x[i]}"
        if i != (n-1): # não é o último elemento
            result += ", "
    result += "]"
    return result

def somar(x):
    return(sum(x))

def media(x):
    if (len(x) == 0):   
        return(0)
    else:
        return(sum(x) / len(x))

def menor_Valor(x):
    if (len(x) == 0):
        return(0)
    else:
        return min(x)

def maior_Valor(x):
    if (len(x) == 0):
        return(0)
    else:
        return max(x)

def toString(id, x):
    result = saida(id, x)
    result += f"\n\nSoma dos Valores  = {somar(x)}\n"
    result += f"Média dos Valores = {media(x):.2f}\n"

    return result
