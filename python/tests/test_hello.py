import python.hello

def test_hello():
    assert python.hello.speak('simon') == 'Hello simon'

def test_hello_does_not_return():
    assert python.hello.speak('some name') != 'Hello some other name'


