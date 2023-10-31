from lab2 import bmi

def test_total_cost_shopping():
    height = 1.73
    weight = 50

    result = bmi.calculate_bmi(height, weight)

    assert result == -1

def test_cost_of_fruit():
    height = 1.73
    weight = 70

    result = bmi.calculate_bmi(height, weight)

    assert result == 0