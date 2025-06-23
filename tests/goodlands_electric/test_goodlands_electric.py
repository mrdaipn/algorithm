from problems.goodlands_electric.good_land_electric import pylons

def test_pylons_basic():
    assert pylons(2, [0, 1, 1, 1, 1, 0]) == 2

def test_pylons_no_possible():
    assert pylons(2, [0, 0, 0, 0, 0]) == -1

def test_pylons_single_plant():
    assert pylons(3, [0, 0, 1, 0, 0]) == 1

def test_pylons_multiple_plants():
    assert pylons(2, [1, 0, 1, 0, 1, 0, 1]) == 4

def test_pylons_all_ones():
    assert pylons(1, [1, 1, 1, 1]) == 4

def test_pylons_large_k():
    assert pylons(10, [1, 0, 0, 0, 0, 0, 0, 0, 0, 1]) == 1

def test_pylons_edge_case():
    assert pylons(2, [1]) == 1
    assert pylons(2, [0]) == -1