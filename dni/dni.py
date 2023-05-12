
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
            primeros_8_caracteres = self.dni[:8]
            es_numero = primeros_8_caracteres.isdigit()
            if es_numero:
                return True
            else:
                raise SyntaxError("est edni no tiene letr al final")

        else:
            raise SyntaxError("est edni no tiene letr al final")
        

    def validar_calculo(self):
        l =["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        resto = int(self.dni[:8]) % 23
        letra = l[resto]
        dni_final = f"{self.dni[:8]}{letra}"
        return dni_final
    

    

if __name__ == "__main__":
    entrada = input("Introduzca un dni 8 Numeros y 1 LETRA: ")
    dni = Dni(entrada)
    dni.validar_calculo()
       

        
        
            
