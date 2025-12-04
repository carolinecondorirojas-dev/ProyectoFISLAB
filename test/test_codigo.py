import unittest
import cod

def test_suma():
    assert cod.suma(2, 3) == 5

def test_multiplicacion():
    assert cod.multiplicacion(2, 3) == 6

if __name__ == '_main_':
    test_suma()
    test_multiplicacion()
    print("Todas las pruebas pasaron.")
