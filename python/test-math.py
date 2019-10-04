def math(numberOne, numberTwo, action):
    if action == 'multiply':
        return numberOne*numberTwo
    if action == 'divide':
        return numberOne/numberTwo
    if action == 'add':
        return numberOne+numberTwo
    if action == 'subtract':
        return numberOne-numberTwo

def test_math_will_fail():
    assert math(2,4,'add') == 5