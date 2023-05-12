from suma_recursiva import SumaRecursiva


def test_crear_valor():
    valor = 3
    objeto = SumaRecursiva(valor)

    assert objeto.valor == valor
