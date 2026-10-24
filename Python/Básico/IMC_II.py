paciente = input("nome do paciente: ")
pc = float(input("peso do paciente (em kg): "))
altura = float(input("altura do paciente (em metros): "))

vlr_IMC = pc / (altura ** 2)

if vlr_IMC < 18.5:
    interpretacao = "Magreza"
else:
    if vlr_IMC < 25:
        interpretacao = "Normal"
    else:
        if vlr_IMC < 30:
            interpretacao = "Sobrepeso"
        else:
            if vlr_IMC < 40:
                interpretacao = "Obesidade"
            else:
                interpretacao = "Obesidade Grave"

print()
print(f"Nome do Paciente: {paciente}")
print(f"Peso Corporal...: {pc:.3f} kg")
print(f"Altura..........: {altura} m")
print(f"Valor do IMC....: {vlr_IMC:.2f} <<< {interpretacao} >>>")