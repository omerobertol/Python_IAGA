# Processamento: Operações Aritméticas
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

# módulo principal (main)
# Entrada de Dados
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número.: "))

# Saída de Dados
print()
print(toString(a, b))