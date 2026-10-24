def digaOla():
    print("Olá!!!")

def digaOlaPara(nome):
    print(f"Olá {nome}!!!")

def boasVindas(nome, sexo):
    if (sexo == "M") or (sexo == "m"):
        print(f"Seja bem-vindo Sr. {nome}!!!")
    else:
        print(f"Seja bem-vinda Sra. {nome}!!!")
    
# módulo principal (main)
digaOla()
print()
digaOlaPara("Maria")
digaOlaPara("João")
print()
boasVindas("Maria", "F")
boasVindas("João", "M")