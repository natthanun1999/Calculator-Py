class Calculator():
    def __init__(self, _L, _R, _OP):
        self.L = _L
        self.R = _R
        self.OP = _OP
        self.Result = 0.0

    def calc(self):
        if (self.OP == "+"):
            self.Result = self.L + self.R
        elif (self.OP == "-"):
            self.Result = self.L - self.R
        elif (self.OP == "*"):
            self.Result = self.L * self.R
        elif (self.OP == "/"):
            self.Result = self.L / self.R
        
        return self.Result
'''
_L = float(input("Enter first number : "))
_OP = input("Enter Operator : ")
_R = float(input("Enter second number : "))

_Result = Calculator(_L, _R, _OP).calc()

print(f"{_L} {_OP} {_R} = {_Result}")
'''