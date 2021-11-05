from divide.another_divide import another_divide


def test_another_divide_positive():
    assert another_divide(3, 2) == 1.5

def test_another_divide_negative():
    assert another_divide(-4, 2) == -2
