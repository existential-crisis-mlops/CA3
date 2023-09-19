from calculator import multiply
from calculator import divide

def test_multiply():
    assert 6 == multiply(3,2)

def test_divide():
    assert 6 == divide(36,6)