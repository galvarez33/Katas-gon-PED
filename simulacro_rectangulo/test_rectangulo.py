from rectangulo import Rectangulo

def test_guarda_punto1():
    punto1 = (2,3)
    obj = Rectangulo(punto1)
    assert obj.punto1 == punto1
