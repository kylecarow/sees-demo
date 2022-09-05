from bisectdemo.calculate import add, subtract, multiply, divide

def test_add():
    assert add(1.0, 1.0) == 2.0
    assert add(2.0, 1.0) == 3.0
    assert add(3.0, 2.0) == 5.0
    assert add(4.0, 2.0) == 6.0
    assert add(5.0, 3.0) == 8.0
    assert add(6.0, 3.0) == 9.0

def test_subtract():
    assert subtract(1.0, 1.0) == 0.0
    assert subtract(2.0, 1.0) == 1.0
    assert subtract(3.0, 2.0) == 1.0
    assert subtract(4.0, 2.0) == 2.0
    assert subtract(5.0, 3.0) == 2.0
    assert subtract(6.0, 3.0) == 3.0

def test_multiply():
    assert multiply(1.0, 1.0) == 1.0
    assert multiply(2.0, 1.0) == 2.0
    assert multiply(3.0, 2.0) == 6.0
    assert multiply(4.0, 2.0) == 8.0
    assert multiply(5.0, 3.0) == 15.0
    assert multiply(6.0, 3.0) == 18.0

def test_divide():
    assert divide(1.0, 1.0) == 1.0
    assert divide(2.0, 1.0) == 2.0
    assert divide(3.0, 2.0) == 1.5
    assert divide(4.0, 2.0) == 2.0
    assert divide(5.0, 3.0) == 1.6666666666666667
    assert divide(6.0, 3.0) == 2.0
