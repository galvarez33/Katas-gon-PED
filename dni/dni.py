
class Dni:

    def __init__(self, dni):
        self.dni = dni
    
    def validar_long(self):
        if len(self.dni) == 9:
            return len(self.dni)
        else:
            raise ValueError("Longitud erronea") 
        
    def validar_formato(self):
        ultimo_caracter = self.dni[-1]
        es_letra = ultimo_caracter.isalpha()
        if es_letra:
            return True
        else:
            raise SyntaxError("est edni no tiene letr al final")
        
        
            
