from rectangulo import Rectangulo

def test_guarda_punto1():
    punto1 = (2,3)
    obj = Rectangulo(punto1)
    assert obj.punto1 == punto1

def test_guarda_punto2():
    punto2 = (2,3)
    obj = Rectangulo(punto2)
    assert obj.punto2 == punto2
