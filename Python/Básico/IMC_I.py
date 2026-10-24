paciente = input("nome do paciente: ")
pc = float(input("peso do paciente (em kg): "))
altura = float(input("altura do paciente (em metros): "))

vlr_IMC = pc / (altura ** 2)

if vlr_IMC < 18.5:
    interpretacao = "Magreza"

if vlr_IMC >= 18.5 and vlr_IMC < 25:
    interpretacao = "Normal"

if vlr_IMC >= 25 and vlr_IMC < 30:
    interpretacao = "Sobrepeso"

if vlr_IMC >= 30 and vlr_IMC < 40:
    interpretacao = "Obesidade"

if vlr_IMC >= 40:
    interpretacao = "Obesidade Grave"

print()
print(f"Nome do Paciente: {paciente}")
print(f"Peso Corporal...: {pc:.3f} kg")
print(f"Altura..........: {altura} m")
print(f"Valor do IMC....: {vlr_IMC:.2f} <<< {interpretacao} >>>")