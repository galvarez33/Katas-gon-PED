from suma_dos_numero import SumaDosNumeros


def test_suma_dos_numeros():
    a = 2
    b = 3
    resultado = SumaDosNumeros.suma(a, b)
    assert resultado == 5

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