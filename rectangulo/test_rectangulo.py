from rectangulo import Rectangulo

def test_constructor_base():
    a = 2
    r = Rectangulo(a)
    assert r.a == a  