# cabeçalho da classe MeuMath (entidade abstrata)
class MeuMath:
# método construtor da classe MeuMath
# este método cria um objeto da classe MeuMath
# os atributos e métodos estão "encapsulados" na classe MeuMath
    def __init__(self, a, b):
        # atributos da classe MeuMath (porção de dados)
        # os atributos são privados, ou seja, 
        # só podem ser acessados dentro da classe MeuMath
        # objetivo é inicializar os atributos da instância 
        # da classe MeuMath
        self.a = a
        self.b = b

# protocolo de métodos da classe MeuMath (interface)
# métodos de acesso da classe: getters e setters
    def get_a(self): # retorna o valor do atributo 'a'
        return self.a

    def set_a(self, a): # modifica o valor do atributo 'a'
        self.a = a

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b

# corpo da classe MeuMath: atributos e métodos
    def soma(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def divInt(self):
        if self.b == 0:
            return 0 # divisão por zero não é possível
        else:
            return self.a // self.b

    def divReal(self):
        if self.b == 0:
            return 0 # divisão por zero não é possível
        else:
            return self.a / self.b

    def resto(self):
        if self.b == 0:
            return 0 # divisão por zero não é possível
        else:
            return self.a % self.b

# método que exibe as informações do objetos
    def __str__(self):
        result = f"{self.a} + {self.b} = {self.soma()}\n"
        result += f"{self.a} - {self.b} = {self.sub()}\n"
        result += f"{self.a} X {self.b} = {self.mult()}\n"
        result += f"{self.a} // {self.b} = {self.divInt()}\n"
        result += f"{self.a} / {self.b} = {self.divReal()}\n"
        result += f"{self.a} % {self.b} = {self.resto()}\n"

        return result

# polimorfismo: várias formas
# polimorfismo de sobrecarga: 
# mesma assinatura, mas comportamentos diferentes
# 
# polimorfismo de sobrescrita: 
# mesma assinatura, mas comportamentos diferentes


# assinatura de um método: 
# nome do método + parâmetros do método