import pytest

def math(numberOne, numberTwo, action):
    if action == 'multiply':
        return numberOne*numberTwo
    if action == 'divide':
        return numberOne/numberTwo
    if action == 'add':
        return numberOne+numberTwo
    if action == 'subtract':
        return numberOne-numberTwo
    raise Exception('Action passed is not supported')

def test_math_will_fail():
    assert math(2,4,'multiply') == 9

def test_assert_that_exception_is_thrown():
    with pytest.raises(Exception):
        math(1,1, 'Not Supported')

def test_assert_that_multiply_returns_the_correct_answer():
    assert math(2,4, 'multiply') == 8

def test_assert_that_add_returns_the_correct_answer():
    assert math(2,2, 'add') == 4

def test_assert_that_subtract_returns_the_correct_answer():
    assert math(3,2, 'subtract') == 1

def test_assert_that_divide_returns_the_correct_answer():
    assert math(6,3, 'divide') == 2
