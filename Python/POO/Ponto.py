class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def posicao(self):
        if self.x > 0 and self.y > 0:
            return "1º Quadrante"
        elif self.x < 0 and self.y > 0:
            return "2º Quadrante"
        elif self.x < 0 and self.y < 0:
            return "3º Quadrante"
        elif self.x > 0 and self.y < 0:
            return "4º Quadrante"
        elif self.x == 0 and self.y != 0:
            return "Eixo Y"
        elif self.x != 0 and self.y == 0:
            return "Eixo X"
        elif self.x == 0 and self.y == 0:
            return "Origem"

    def __str__(self):
        return f"(x: {self.x}, y: {self.y}) = {self.posicao()}"

# por exemplo (__str__):
# (1, 1) = 1º Quadrante
# (-1, 1) = 2º Quadrante
# (-1, -1) = 3º Quadrante
# (1, -1) = 4º Quadrante
# (0, 1) = Eixo Y
# (1, 0) = Eixo X
# (0, 0) = Origem