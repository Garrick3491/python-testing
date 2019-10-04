def hello(name):
    return 'Hello ' + name

def test_hello():
    assert hello('simon') == 'Hello simon'

def test_hello_does_not_return():
    assert hello('some name') != 'Hello some other name'


