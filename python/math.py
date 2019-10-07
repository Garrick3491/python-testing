def calculate(numberOne, numberTwo, action):
    if action == 'multiply':
        return numberOne*numberTwo
    if action == 'divide':
        return numberOne/numberTwo
    if action == 'add':
        return numberOne+numberTwo
    if action == 'subtract':
        return numberOne-numberTwo
    raise Exception('Action passed is not supported')