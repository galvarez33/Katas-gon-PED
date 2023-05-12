
class SumaDosNumeros:
    def __init__(self,a,b):
       self.a = a
       self.b = b


    def es_entero(self, a, b):
       try:
          float(self.a)
          float(self.b)
          return True
       except:
          return False


    def suma(a, b):
        if not SumaDosNumeros.es_entero(a,b):
           raise ValueError("Valor no valido")

        a = float(a)
        b = float(b)
        return a + b 
    
           
        