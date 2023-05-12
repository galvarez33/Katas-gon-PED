class Rectangulo:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError("No puede ser negativo")
        else:
            return self.a * self.b
    
    def perimetro(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError("No puede ser negativo")
        else:
            return self.a *2 + self.b * 2 