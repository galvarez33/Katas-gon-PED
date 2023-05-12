from suma_recursiva import SumaRecursiva


def test_crear_valor():
    valor = 3
    objeto = SumaRecursiva(valor)

    assert objeto.valor == valor

def test_suma_recursiva():
    n = 5
    resultado_esperado = 15 #1+2+3+4+5
    sumador = SumaRecursiva(n)
    resultado = sumador.suma_recursiva()

    assert resultado_esperado == resultado

