import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_case1(self):
        _L = 45.0
        _R = 5.0
        _OP = '+'
        _Result = 50.0

        myCalc = Calculator(_L, _R, _OP)
        self.assertEqual(myCalc.calc(), _Result, f"{_L} {_OP} {_R}")
        
        print(f"Case {_L} {_OP} {_R} Passed")
    
    def test_case2(self):
        _L = 45.0
        _R = 5.0
        _OP = '-'
        _Result = 40.0

        myCalc = Calculator(_L, _R, _OP)
        self.assertEqual(myCalc.calc(), _Result, f"{_L} {_OP} {_R}")
        
        print(f"Case {_L} {_OP} {_R} Passed")
    
    def test_case3(self):
        _L = -12.5
        _R = 2.5
        _OP = '+'
        _Result = -10.0

        myCalc = Calculator(_L, _R, _OP)
        self.assertEqual(myCalc.calc(), _Result, f"{_L} {_OP} {_R}")
        
        print(f"Case {_L} {_OP} {_R} Passed")
    
    def test_case4(self):
        _L = 12.0
        _R = 5.0
        _OP = '*'
        _Result = 60.0

        myCalc = Calculator(_L, _R, _OP)
        self.assertEqual(myCalc.calc(), _Result, f"{_L} {_OP} {_R}")
        
        print(f"Case {_L} {_OP} {_R} Passed")

    def test_case5(self):
        _L = 45.0
        _R = 5.0
        _OP = '/'
        _Result = 9.0

        myCalc = Calculator(_L, _R, _OP)
        self.assertEqual(myCalc.calc(), _Result, f"{_L} {_OP} {_R}")
        
        print(f"Case {_L} {_OP} {_R} Passed")

if __name__ == '__main__':
    unittest.main()