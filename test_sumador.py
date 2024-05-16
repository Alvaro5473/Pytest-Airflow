from sumador import sumar

def test_suma_correcta():
    assert sumar(2, 3) == 5

def test_suma_incorrecta():
    assert sumar(1, 1) != 3