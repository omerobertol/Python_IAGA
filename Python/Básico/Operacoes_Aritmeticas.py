# Entrada de Dados
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número.: "))

# Processamento: Operações Aritméticas
soma = a + b
sub = a - b
mult = a * b
divInt = a // b
divReal = a / b
resto = a % b

# Saída de Dados
print()
print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {sub}")
print(f"{a} X {b} = {mult}")
print(f"{a} // {b} = {divInt} divisão inteira")
print(f"{a} / {b} = {divReal} divisão real")
print(f"{a} % {b} = {resto} resto da divisão")