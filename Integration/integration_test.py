# integration_test.py
from even_numbers import is_odd
from even_numbers import is_even
def test_even_number():
    assert is_even(4) == True
def test_odd_number():
    assert is_even(7) == False
def test_odd_number_2():
    assert is_even(9) == False
