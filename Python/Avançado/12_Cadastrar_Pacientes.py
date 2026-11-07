import Geral

Geral.cls()

# 1. abre o arquivo de texto (mode de abertura 'a' - append)
arquivo = open("pacientes.txt", "a")

n = int(input("Digite a quantidade de pacientes: "))

for i in range(n):
    Geral.cls()
    print(f"{i+1}o. paciente")
    paciente = input("Nome do paciente......: ")
    pc = float(input("Peso Corporal (em kgs): "))
    alt = float(input("Altura (em metros)....: "))

    if Geral.confirmou("\nCadastrar Paciente (s/n)? "):
        # 2. grava a linha no arquivo de texto
        arquivo.write(f"{paciente};{pc};{alt}\n")
        
        print("Paciente cadastrado com sucesso!!!")
        Geral.delay(1) # tempo de 1 segundo

# 3. Fechando o arquivo texto
arquivo.close()