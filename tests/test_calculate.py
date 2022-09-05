from bisectdemo.calculate import multiply

def test_multiply():
    assert multiply(1.0, 1.0) == 1.0
    assert multiply(2.0, 1.0) == 2.0
    assert multiply(3.0, 2.0) == 6.0
    assert multiply(4.0, 2.0) == 8.0
    assert multiply(5.0, 3.0) == 15.0
    assert multiply(6.0, 3.0) == 18.0
