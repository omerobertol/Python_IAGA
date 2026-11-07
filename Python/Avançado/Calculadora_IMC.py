def calcular_IMC(pc, alt):
    return pc / (alt ** 2)

def interpretar_IMC(vlr_IMC):
    if vlr_IMC < 18.5:
        interpretacao = "Magreza"
    elif vlr_IMC < 25:
        interpretacao = "Normal"
    elif vlr_IMC < 30:
        interpretacao = "Sobrepeso"
    elif vlr_IMC < 40:
        interpretacao = "Obesidade"
    else:
        interpretacao = "Obesidade Grave"

    return interpretacao

def toString(paciente, pc, alt):
    vlr_IMC = calcular_IMC(pc, alt)
    interpretacao = interpretar_IMC(vlr_IMC)

    result = f"Nome do Paciente: {paciente}\n"
    result += f"Peso Corporal...: {pc:.3f} kg\n"
    result += f"Altura..........: {alt:.2f} m\n"
    result += f"Valor do IMC....: {vlr_IMC:.2f} <<< {interpretacao} >>>"

    return result