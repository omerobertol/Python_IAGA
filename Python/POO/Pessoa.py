from Data import Data

class Pessoa:
    def __init__(self, nome, sexo, dtNasc):
        self.nome = nome
        self.sexo = sexo
        # Relacionamento de Associação
        # estabelece um link entre a classe Pessoa e 
        # a classe 'Data' através do atributo 'dtNasc'
        self.dtNasc = dtNasc

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getSexo(self):
        return self.sexo

    def setSexo(self, sexo):
        self.sexo = sexo

    def getDtNasc(self):
        return self.dtNasc

    def setDtNasc(self, dtNasc):
        self.dtNasc = dtNasc

    def __str__(self):
        result = f"Nome............: {self.nome}\n"
        result += f"Sexo............: {self.sexo}\n"
        result += f"Nascimento......: {self.dtNasc.toString(mostrarIdade=True)}\n"

        return result