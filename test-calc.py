import unittest
from calc import calculator

mycalc = calculator(10,5)
class test_calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mycalc.add(),15)
    # def test_subtract(self):
    #     self.assertEqual(mycalc.subtract(),5)
    # def test_multiply(self):
    #     self.assertEqual(mycalc.multiply(),50)
    # def test_divide(self):
    #     self.assertEqual(mycalc.divide(),2)
    pass

if __name__ == "__main__":
    unittest.main()    
    
