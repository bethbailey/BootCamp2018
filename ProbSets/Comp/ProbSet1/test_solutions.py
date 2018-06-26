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
    with pytest.raises(TypeError) as excinfo:
        soln.operate(4, 0, 0)
    assert excinfo.value.args[0] == "Oper should be a string"
    # with pytest.raises(ValueError) as excinfo:
    #     soln.operator(4, 0, "+-")
    # assert excinfo.value.args[0] == "oper must be..., -', or '*'"
    with pytest.raises(ValueError) as excinfo:
        soln.operate(4, 0, ")")
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"
    assert soln.operate(1, 2, "+")==3, "Failed for adding"
    assert soln.operate(1, 2, "-") == -1, "Failed for minusing"
    assert soln.operate(1, 2, "*") == 2, "Failed for multiplying"
    assert soln.operate(2, 1, "/") == 2, "Failed for dividing"
    with pytest.raises(ZeroDivisionError) as excinfo:
        soln.operate(4, 0, "/")
    assert excinfo.value.args[0] == "division by zero is undefined"

# Problem 4: test cases for fraction.
from soln import Fraction

@pytest.fixture
def set_up_fractions():
    frac_1_3 = soln.Fraction(1, 3)
    frac_1_2 = soln.Fraction(1, 2)
    frac_n2_3 = soln.Fraction(-2, 3)
    return frac_1_3, frac_1_2, frac_n2_3

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = soln.Fraction(30, 42) # 30/42 reduces to 5/7.
    assert frac.numer == 5
    assert frac.denom == 7
    with pytest.raises(ZeroDivisionError) as excinfo:
        soln.Fraction(1, 0)
    assert excinfo.value.args[0] == "denominator cannot be zero"
    with pytest.raises(TypeError) as excinfo:
        soln.Fraction(1., 2.)
    assert excinfo.value.args[0] == "numerator and denominator must be integers"

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(frac_1_3) == "1 / 3"
    assert str(frac_1_2) == "1 / 2"
    assert str(frac_n2_3) == "-2 / 3"
    assert str(Fraction(2, 1)) == "2"

def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == soln.Fraction(1, 2)
    assert frac_1_3 == soln.Fraction(2, 6)
    assert frac_n2_3 == soln.Fraction(8, -12)
    assert soln.Fraction(1, 2) == 2 / 4.

def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 + frac_1_2 == soln.Fraction(5, 6)
    assert frac_1_3 + frac_n2_3 == soln.Fraction(-1, 3)
    assert frac_1_2 + frac_n2_3 == soln.Fraction(-1, 6)

def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 - frac_1_2 == soln.Fraction(-1, 6)
    assert frac_1_3 - frac_n2_3 == soln.Fraction(3, 3)
    assert frac_1_2 - frac_n2_3 == soln.Fraction(7, 6)

def test_fraction_mult(set_up_fractions): 
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 * frac_1_2 == soln.Fraction(1, 6)
    assert frac_1_3 * frac_n2_3 == soln.Fraction(-2, 9)
    assert frac_1_2 * frac_n2_3 == soln.Fraction(-2, 6)

def test_fraction_truediv(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 / frac_1_2 == soln.Fraction(2, 3)
    assert frac_1_3 / frac_n2_3 == soln.Fraction(-1, 2)
    assert frac_1_2 / frac_n2_3 == soln.Fraction(-3, 4)
    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_1_3 / soln.Fraction(0, 1)
    assert excinfo.value.args[0] == "cannot divide by zero"

# Problem 5: Write test cases for the Set game.
@pytest.fixture
def set_up_cards():
    cards_1 = ["1022", "1122", "1020"]
    cards_2 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0)10", "2110", "1020"]
    cards_3 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "010", "2110", "1020"]
    cards_4 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0210", "2111", "1020"]
    cards_5 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0510", "2110", "1020"]
    cards_6 = ["1022", "1122", "0100", "2021",
               "0010", "2201", "2111", "0020",
               "1102", "0210", "2110", "1020"]
    return cards_1, cards_2, cards_3, cards_4, cards_5, cards_6

def test_set(set_up_cards):
    cards_1, cards_2, cards_3, cards_4, cards_5, cards_6 = set_up_cards
    assert soln.count_sets(cards_6) == 6, "Not counting cards correctly"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_1)
    assert excinfo.value.args[0] == "there are not exactly 12 cards"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_2)
    assert excinfo.value.args[0] == "one or more cards has a character other than 0, 1, or 2"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_3)
    assert excinfo.value.args[0] == "one or more cards does not have exactly 4 digits"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_4)
    assert excinfo.value.args[0] == "the cards are not all unique"
    with pytest.raises(ValueError) as excinfo:
        soln.count_sets(cards_5)
    assert excinfo.value.args[0] == "one or more cards has a character other than 0, 1, or 2"
