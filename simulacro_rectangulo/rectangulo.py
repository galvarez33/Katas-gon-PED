class Rectangulo:

    def __init__(self, punto1, punto2):
        if isinstance(punto1, tuple) and isinstance(punto2, tuple):
                self.punto1 = punto1
                self.punto2 = punto2
        else:
            raise ValueError("Formato de punto incorrecto")

    def crear_puntos(self):
        if self.punto1 != self.punto2 and self.punto1[0] != self.punto2[0] and self.punto1[1] != self.punto2[1]  :
            punto3 = (self.punto2[0], self.punto1[1])
            punto4 = (self.punto1[0], self.punto2[1])
            return punto3, punto4
        else:
            raise ValueError("Has pasado dos puntos iguales o 2 x iguales o dos y iguales")
        
    def crear_rectangulo(self):
        punto3, punto4 = self.crear_puntos()
        l = [self.punto1,self.punto2, punto3, punto4]
        return l
    
    def calcular_area(self):
        base = self.punto2[0]- self.punto1[0]
        altura = self.punto2[1]- self.punto1[1]
        area = base * altura
        return area 
    
    def calcular_perimetro(self):
        perimetro = (self.punto2[0]- self.punto1[0])*2 + (self.punto2[1]- self.punto1[1])*2
        return perimetro
    
    
        
        