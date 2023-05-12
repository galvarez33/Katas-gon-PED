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

def test_calcular_area():
    a = 2
    b = 2
    r = Rectangulo(a,b).area()
    assert r == 4

def test_calcular_area2():
    a = 3
    b = 2
    r = Rectangulo(a,b).area()
    assert r == 6

def test_calcular_area3():
    a = 3
    b = 3
    r = Rectangulo(a,b).area()
    assert r == 9