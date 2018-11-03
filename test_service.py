from service import Service
from unittest.mock import patch

service = Service()

@patch('service.Service.bad_random', return_value=10)
def test_bad_random(bad_random):
    assert service.bad_random() == 10

@patch('service.Service.bad_random', return_value=10)
def test_divide(bad_random):
    assert service.divide(10) == 1
    assert service.divide(1) == 10
    assert service.divide(-1) == -10
    assert service.divide(2) == 5
    assert service.divide(0.5) == 20

def test_abs_plus():
    assert service.abs_plus(-1) == 2
    assert service.abs_plus(1) == 2
    assert service.abs_plus(0) == 1
    assert service.abs_plus(-0.5) == 1.5

@patch('service.Service.bad_random', return_value=10)
def test_complicated_function(bad_random):
    assert service.complicated_function(10) == (1, 0)
    assert service.complicated_function(-2) == (-5, 0)
    assert service.complicated_function(0.5) == (20, 0)
