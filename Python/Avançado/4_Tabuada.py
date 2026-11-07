def tabuada_I(n):
    i = 1 # variável de controle do laço de repetição
    while i <= 10:
        print(f"{n} X {i} = {n * i}")
        i = i + 1 # incremento da variável de controle do laço de repetição

def tabuada_II(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n * i}")

# módulo principal (main)
while True:
    n = int(input("De 0 até 10, -1 para encerrar: "))
    if n == -1:
        break
    elif n < 0 or n > 10:
        print(f"{n}, número inválido! Digite um número de 0 até 10.")
    else:
        print()
        tabuada_I(n) # na versão com while, a tabuada é impressa de 1 até 10
        print()
        tabuada_II(n) # na versão com for, a tabuada é impressa de 1 até 10
    
    print()