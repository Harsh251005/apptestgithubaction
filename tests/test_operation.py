from src.math_operations import add, sub

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 10) == 10
    assert add(1, 1) == 2

def test_sub():

    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(6, 1) == 5
    assert sub(10, 1) == 9