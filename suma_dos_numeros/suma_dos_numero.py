
class SumaDosNumeros:
    def __init__(self,a,b):
       self.a = a

    def es_entero(a,b):
       try:
          float(a)
          float(b)
          return True
       except:
          return False


    def suma(a, b):
        if not SumaDosNumeros.es_entero(a,b):
           raise ValueError("Valor no valido")

        a = float(a)
        b = float(b)
        return a + b 
    
           
        