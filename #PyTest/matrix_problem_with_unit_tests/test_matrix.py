from matrix import stringify_matrix, smallest_in_the_column, smallest_in_the_row

def test_print_matrix():
    output = stringify_matrix([[1, 2, 3], [4, 5, 6]])
    expected_output = '1 2 3\n4 5 6\n'
    assert output == expected_output
    
def test_smallest_in_the_column():
    output = smallest_in_the_column([[1, 2, 3], [4, 5, 6]], 1)
    assert output == (0, 1)

def test_smallest_in_the_row():
    output = smallest_in_the_row([[1, 2, 3], [4, 5, 6]], 1)
    assert output == (1, 0)