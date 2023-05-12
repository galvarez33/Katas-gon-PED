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
    
    def ejecutar(self):
        a = float(input("Ingrese el valor de la base: "))
        b = float(input("Ingrese el valor de la altura: "))
        self.a = a
        self.b = b

        print("Área:", self.area())
        print("Perímetro:", self.perimetro())
    
if __name__ == "__main__":
    r = Rectangulo(0, 0)
    r.ejecutar()
