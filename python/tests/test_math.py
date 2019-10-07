import pytest
import python.math

def test_math_will_fail():
    assert python.math.calculate(2,4,'multiply') == 9

def test_assert_that_exception_is_thrown():
    with pytest.raises(Exception):
        python.math.calculate(1,1, 'Not Supported')

def test_assert_that_multiply_returns_the_correct_answer():
    assert python.math.calculate(2,4, 'multiply') == 8

def test_assert_that_add_returns_the_correct_answer():
    assert python.math.calculate(2,2, 'add') == 4

def test_assert_that_subtract_returns_the_correct_answer():
    assert python.math.calculate(3,2, 'subtract') == 1

def test_assert_that_divide_returns_the_correct_answer():
    assert python.math.calculate(6,3, 'divide') == 2
