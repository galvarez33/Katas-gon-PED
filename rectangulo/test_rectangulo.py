from rectangulo import Rectangulo

def test_constructor_altura():
    a = 2
    b = 2
    r = Rectangulo(a, b)
    assert r.a == a  

def test_constructor_base():
    a = 2
    b = 2
    r = Rectangulo(a, b)
    assert r.b == b