from dni import Dni

def test_store_dni():
    dni = "12345678N"
    obj = Dni(dni)
    assert obj.dni == dni

def test_comrpobar_longitud():
    dni = "12345678N"
    assert Dni(dni).validar_long() == 9

def test_longitud_erronea():
    dni = "12345678"
    try:
        Dni(dni).validar_long()
        assert False, "No deberia pasar"
    except ValueError:
        assert True