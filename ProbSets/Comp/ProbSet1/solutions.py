# solutions.py
"""Volume IB: Testing.
<Name>
<Date>
"""
import math

# Be sure to install pytest-cov in order to see your code coverage change.

## Problem 1: Additiona and smallest factor.
def addition(a, b):
    return a + b

def smallest_factor(n):
    """Finds the smallest prime factor of a number.
    Assume n is a positive integer.
    """
    if n == 1:
        return 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n

## Problem 2: Month.
def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July",
                        "August", "October", "December"}:
        return 31
    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None

# Problem 3 Write unit tests for operate(). 
def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ZeroDivisionError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")

# def operator(a, b, oper):
#     if type(oper) != str:
#         raise ValueError("Oper should be a string")
#     if len(oper) != 1:
#         raise ValueError("Oper should be one character")
#     if oper == "+":
#         return a + b
#     if oper == "/":
#         if b == 0:
#             raise ValueError("You can't divide by zero!")
#         return a/float(b)
#     if oper == "-":
#         return a-b
#     if oper == "*":
#         return a*b
#     else:
#         raise ValueError("Oper can only be: '+', '/', '-', or '*'")

# Problem 3 Write unit test for this class.
class ComplexNumber(object):
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def norm(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag)

    def __mul__(self, other):
        real = self.real*other.real - self.imag*other.imag
        imag = self.imag*other.real + other.imag*self.real
        return ComplexNumber(real, imag)

    def __truediv__(self, other):
        if other.real == 0 and other.imag == 0:
            raise ValueError("Cannot divide by zero")
        bottom = (other.conjugate()*other*1.).real
        top = self*other.conjugate()
        return ComplexNumber(top.real / bottom, top.imag / bottom)

    def __eq__(self, other):
        return self.imag == other.imag and self.real == other.real

    def __str__(self):
        return "{}{}{}i".format(self.real, '+' if self.imag >= 0 else '-',
                                                                abs(self.imag))

# Problem 5: Write code for the Set game here
