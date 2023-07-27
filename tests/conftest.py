import pytest
from accum.accum import Accumulator

@pytest.fixture(scope='module')
def accumul():
    return Accumulator()
@pytest.fixture(scope='function')
def accumul_2():
    return Accumulator()