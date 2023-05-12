from suma_dos_numero import SumaDosNumeros


def test_suma_dos_numeros():
    assert SumaDosNumeros.suma(2, 3) == 5

def test_suma_dos_numeros_a_erroneo():
    a = "hola"
    b = 3
    try:
        SumaDosNumeros.suma(a,b)
        assert False, "Se esperaba excepcion"
    except ValueError:
        assert True

def test_suma_dos_numeros_b_erroneo():
    a = 2
    b = "hola"
    try:
        SumaDosNumeros.suma(a,b)
        assert False, "Se esperaba excepcion"
    except ValueError:
        assert True

def test_suma_numeros_negativos():
    assert SumaDosNumeros.suma(-2, -3) == -5

def test_suma_dos_numeros_decimales():
    assert SumaDosNumeros.suma(12.5, 7.5) == 20

def test_guarda_primer_valor():
    a = 1
    b = 2
    resultado = SumaDosNumeros(a,b)
    assert resultado.a == a

def test_guarda_segundo_valor():
    a = 1
    b = 2
    resultado = SumaDosNumeros(a,b)
    assert resultado.b == b
   