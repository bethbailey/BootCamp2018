# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest

# Problem 1: Test the addition and smallest factor fuctions.
def test_addition():
    assert soln.addition(1, 3) == 4, "failed on positive integers"
    assert soln.addition(-5, -7) == -12, "failed on negative integers"
    assert soln.addition(-6, 14) == 8
    assert soln.addition(0, 0) == 0

def test_smallest_factor():
    assert soln.smallest_factor(1) == 1, "failed on 1"
    assert soln.smallest_factor(2) == 2, "failed on 2"
    assert soln.smallest_factor(4) == 2, "failed on 4 (squared)"
    assert soln.smallest_factor(3) == 3, "failed on 7 (prime)"
    assert soln.smallest_factor(6) == 2, "failed on 6 (composite)"

## Problem 2: Test month function.
def test_month():
    assert soln.month_length("April")==30, "failed for 30-day months"
    assert soln.month_length("January") == 31, "failed for 31-day months"
    assert soln.month_length("February") == 28, "failed for non-leap feb"
    assert soln.month_length("February", True) == 29, "failed for leap feb"
    assert soln.month_length("Apr") == None, "failed for shortened month/non-month"

# Problem 3: Test the operate function from solutions.py
def test_operate():
    

# def test_operator():
#     pass

# Problem 3: Finish testing the complex number class
@pytest.fixture
def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

# Problem 4: Write test cases for the Set game.
