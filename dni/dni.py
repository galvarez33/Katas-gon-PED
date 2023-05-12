
class Dni:

    def __init__(self, dni):
        self.dni = dni
    
    def validar_long(self):
        if len(self.dni) == 9:
            return len(self.dni)
        else:
            raise ValueError("Longitud erronea") 
            
