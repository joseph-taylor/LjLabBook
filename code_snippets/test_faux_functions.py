from faux_package.faux_functions import calc_add, calc_mult

# run unit tests with $ py.test

def test_calc_add():
    assert calc_add(11,7) == 18

def test_calc_mult():
    assert calc_mult(11,7) == 77