
class SumaRecursiva:
    
    def __init__(self, valor):
        self.valor = valor
    
    def suma_recursiva(self):
        if self.valor == 0:
            return 0
        else:
            return self.valor + SumaRecursiva(self.valor -1).suma_recursiva()