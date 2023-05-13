from rectangulo import Rectangulo

def test_guarda_punto1():
    punto1 = (2,3)
    punto2 = (2,3)
    obj = Rectangulo(punto1, punto2)
    assert obj.punto1 == punto1

def test_guarda_punto2():
    punto1 = (2,3)
    punto2 = (2,3)
    obj = Rectangulo(punto1, punto2)
    assert obj.punto2 == punto2

def test_punt1_debe_ser_tupla():
    punto1 = (3)
    punto2 = (2,3)
    try:
        obj = Rectangulo(punto1, punto2)
        isinstance(obj.punto1, tuple)
        assert False
    except ValueError:
        assert True

