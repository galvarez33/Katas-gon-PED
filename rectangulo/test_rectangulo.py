from rectangulo import Rectangulo

def test_constructor_base():
    a = 2
    r = Rectangulo(a)
    assert r.a == a  

def test_constructor_base():
    b = 2
    r = Rectangulo(b)
    assert r.b == b