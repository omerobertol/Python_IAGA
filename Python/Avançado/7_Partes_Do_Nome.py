def primeiros_Nomes(nome):
    partes_Do_Nome = nome.split(" ")
    n = len(partes_Do_Nome)

    result = ""
    for i in range(n-1):
        result += partes_Do_Nome[i] + " "
    return result

def sobrenome(nome):
    partes_Do_Nome = nome.split(" ")
    n = len(partes_Do_Nome)

    return partes_Do_Nome[n-1]

# módulo principal (main)
while True:
    nome = input("Digite o nome completo (FIM para encerrar):\n")
    if nome.upper() == "FIM":
        break

    print()
    print(f"Primeiros nomes: {primeiros_Nomes(nome)}")
    print(f"Sobrenome......: {sobrenome(nome)}\n")
