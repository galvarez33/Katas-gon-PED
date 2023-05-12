from suma_dos_numero import SumaDosNumeros


def test_suma_dos_numeros():
    a = 2
    b = 3
    resultado = SumaDosNumeros.suma(a, b)
    assert resultado == 5