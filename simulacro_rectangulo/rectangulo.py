class Rectangulo:

    def __init__(self, punto1, punto2):
        if isinstance(punto1, tuple) and isinstance(punto2, tuple):
            self.punto1 = punto1
            self.punto2 = punto2
        else:
            raise ValueError("Formato de punto incorrecto")

    
