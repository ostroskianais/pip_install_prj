from pytest import approx

from pip_install_prj.calculator_functions import square_value

def test_square():

    assert square_value(2) == approx(4)