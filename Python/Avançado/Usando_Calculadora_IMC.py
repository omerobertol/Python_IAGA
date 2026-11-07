from Geral import confirmou, cls
from Calculadora_IMC import toString

cls()
while True:
    paciente = input("Digite o nome do paciente (ou <FIM> para encerrar):\n")
    if paciente.upper() == "FIM":
        break

    print()
    pc = float(input("Digite o peso do paciente (em kg)......: "))
    alt = float(input("Digite a altura do paciente (em metros): "))
    print()

    if confirmou("Deseja calcular o IMC do paciente (s/n)? "):
        print()
        print(toString(paciente, pc, alt))

    print()