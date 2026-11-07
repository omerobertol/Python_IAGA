import Calculadora_IMC
from Geral import cls

cls()

# 1. abre o arquivo de texto (mode de abertura 'r' - read)
arquivo = open("C:\Exemplos\pacientes.txt", "r")

# 2. lê "todas" as linhas do arquivo de texto
linhas = arquivo.readlines()

for linha in linhas: # for each: recupera linha por linha
    partes = linha.split(";") # separa a linha em partes

    paciente = partes[0]
    pc = float(partes[1])
    alt = float(partes[2])

    print(Calculadora_IMC.toString(paciente, pc, alt))          
    print()

# 3. Fechando o arquivo texto
arquivo.close()