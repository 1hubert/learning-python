import algo

def test_area():
    output = algo.area_od_rectangle(5, 6)
    assert output == 30
    
def test_perimeter():
    output = algo.perimeter_of_rectangle(2, 3)
    assert output == 10