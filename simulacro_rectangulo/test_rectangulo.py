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


def test_crear_p3_y_p4_rectangulo():
    punto1 = (1,1)
    punto2 = (3,2)
    obj = Rectangulo(punto1, punto2)
    p3 = (3, 1)
    p4 =(1, 2)
   
    assert obj.crear_puntos() == (p3, p4)

def test_guarda_puntos_lista():
    punto1 = (1,1)
    punto2 = (3,2)
    obj = Rectangulo(punto1, punto2)
    puntos = obj.crear_rectangulo()
    assert puntos == [(1,1),(3,2),(3,1),(1,2)]

def test_area_rectangulo():
    punto1 = (1, 1)
    punto2 = (3, 4)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 6

def test_area_rectangulo2():
    punto1 = (1, 1)
    punto2 = (2, 3)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 2

def test_area_rectangulo_negaitvo():
    punto1 = (-1, -1)
    punto2 = (-3, -2)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 2

def test_area_rectangulo_decimales():
    punto1 = (1.5, 2.5)
    punto2 = (3.5, 4.5)
    obj = Rectangulo(punto1, punto2)
    area = obj.calcular_area()
    assert area == 4.0






