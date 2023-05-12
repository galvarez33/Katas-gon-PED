
class SumaDosNumeros:

    def suma(a, b):
        try:
          a = float(a)
          b = float(b)
          return a + b 
        except:
           raise ValueError("Valor no valido")
        