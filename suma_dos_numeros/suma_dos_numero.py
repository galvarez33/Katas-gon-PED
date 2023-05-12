
class SumaDosNumeros:

    def suma(a, b):
        try:
          a = int(a)
          b = int(b)
          return a + b 
        except:
           raise ValueError("Valor no valido")
        