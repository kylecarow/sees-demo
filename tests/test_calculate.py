from bisectdemo.calculate import add, subtract, multiply

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
