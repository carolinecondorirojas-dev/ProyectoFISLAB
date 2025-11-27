import unittest
import cod

class TestCod(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(cod.suma(2, 3), 5) 

    def test_multiplicacion(self):
        self.assertEqual(cod.multiplicacion(2, 3), 6)  


if __name__ == '__main__':
    unittest.main()