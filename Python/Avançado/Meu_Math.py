# um módulo equivale a uma função

# trecho de código que pode ser reutilizado 
# em outros programas
def soma(a, b): # a, b são parâmetros
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def divInt(a, b):
    if b == 0:
        return 0 # divisão por zero não é possível
    else:
        return a // b

def divReal(a, b):
    if b == 0:
        return 0 # divisão por zero não é possível
    else:
        return a / b

def resto(a, b):
    if b == 0:
        return 0 # divisão por zero não é possível
    else:
        return a % b
    
def toString(a, b):
    result = f"{a} + {b} = {soma(a, b)}\n"
    result += f"{a} - {b} = {sub(a, b)}\n"
    result += f"{a} X {b} = {mult(a, b)}\n"
    result += f"{a} // {b} = {divInt(a, b)} divisão inteira\n"
    result += f"{a} / {b} = {divReal(a, b)} divisão real\n"
    result += f"{a} % {b} = {resto(a, b)} resto da divisão\n"
    
    return result

# 10 seus divisores são 1, 2, 5 e 10
# 11 seus divisores são 1 e 11
def divisores(n):
    div = []
    for i in range(1, n+1):
        if n % i == 0:
            div.append(i)
    return div

def ehPrimo(n):
    return len(divisores(n)) == 2


