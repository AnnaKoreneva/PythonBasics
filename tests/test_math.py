import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_one_error():
    assert 1 + 3 == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert "division by zero" in str(e.value)


params = [
    (2, 3, 6),
    (-2, 3, -6),
    (2, 0, 0),
    (2, 1, 2),
    (-5, -5, 25),
    (0.5, 0.5, 0.25)
]


@pytest.mark.math
@pytest.mark.parametrize('a, b, result', params)
def test_multiplication(a, b, result):
    assert a * b == result
