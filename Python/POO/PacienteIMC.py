from Pessoa import Pessoa
import sys
sys.path.append("C:\Python_IAGA\Python\Avançado")
from Calculadora_IMC import calcular_IMC, interpretar_IMC

class PacienteIMC(Pessoa):

    def __init__(self, nome, sexo, dataNascimento, pc, alt):
        super().__init__(nome, sexo, dataNascimento)
        # estou "especializando" a classe Filho
        self.pc = pc
        self.alt = alt

    def getPC(self):
        return self.pc

    def setPC(self, pc):
        self.pc = pc

    def getAlt(self):
        return self.alt

    def setAlt(self, alt):
        self.alt = alt

    def __str__(self):
        result = super().__str__()
        result += f"Peso Corporal...: {self.pc:.3f} kg\n"
        result += f"Altura..........: {self.alt:.2f} m\n"

        vlr_IMC = calcular_IMC(self.pc, self.alt)
        interpretacao = interpretar_IMC(vlr_IMC)
        result += f"Valor do IMC....: {vlr_IMC:.2f} <<< {interpretacao} >>>"

        return result




# Pessoa            PacienteIMC (Herança)
# Pai               Filho
# Base              Derivada
# SuperClasse       Subclasse
# Generalização     Especialização
# (geral)           (específico, ele evolui a partir da classe pai)

# COM PROPÓSITO DE "REUTILIZAÇÃO DE CÓDIGO"