import pytest
import mathlib

# An example of replacing repetetive tests 
# with parametrization
@pytest.mark.parametrize("test_input, expected_output", [
    (5, 25), 
    (3, 9), 
    (5, 25)
])
def test_calc_square(test_input, expected_output):
    result = mathlib.calc_square(test_input)
    assert result == expected_output
