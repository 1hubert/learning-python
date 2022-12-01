import calculator

def test_square_root():
    """Verify the output of `square root` function."""
    output = calculator.square_root(64)
    assert output == 8
    
def test_division_by_n():
    """Verify the output of `division_by_n` function."""
    output = calculator.division_by_n(90, 2)
    assert output == 45
