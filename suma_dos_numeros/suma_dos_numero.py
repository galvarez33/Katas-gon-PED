
class SumaDosNumeros:


    def es_entero(a,b):
       try:
          float(a)
          float(b)
          return True
       except:
          return False


    def suma(a, b):
        if not es_entero(a,b):
           raise ValueError("Valor no valido")

        a = float(a)
        b = float(b)
        return a + b 
    
           
        