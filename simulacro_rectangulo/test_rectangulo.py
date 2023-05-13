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

def test_punto1_debe_ser_tupla():
    punto1 = (3)
    punto2 = (2,3)
    try:
        obj = Rectangulo(punto1, punto2)
        isinstance(obj.punto1, tuple)
        assert False
    except ValueError:
        assert True

def test_punto2_debe_ser_tupla():
    punto1 = (3,2)
    punto2 = (2)
    try:
        obj = Rectangulo(punto1, punto2)
        isinstance(obj.punto2, tuple)
        assert False
    except ValueError:
        assert True

def test_crear_rectangulo1():
    punto1 = (1,1)
    punto2 = (3,2)
    obj = Rectangulo(punto1, punto2)
    p3 =(3,1)
    p4 = (1,2)
    
    assert obj.crear_rectangulo() == (p3, p4)
