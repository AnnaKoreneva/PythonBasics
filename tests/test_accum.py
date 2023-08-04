import pytest

@pytest.mark.accumulator
def test_accumulator_init(accumul, accumul_2):
    assert accumul.count == 0
@pytest.mark.accumulator
def test_accum_add_one(accumul):
    accumul.add()
    assert accumul.count == 1

@pytest.mark.accumulator
def test_accum_add_two(accumul):
    accumul.add()
    accumul.add()
    assert accumul.count == 2

@pytest.mark.accumulator
def test_accum_add_three(accumul):
    accumul.add(3)
    assert accumul.count == 3

def test_accum_add_string(accumul):
    with pytest.raises(TypeError):
        accumul.add('www')

def test_accum_no_setters(accumul):
    with pytest.raises(AttributeError, match="property 'count' of 'Accumulator' object has no setter"):
        accumul.count  = 10