import lab2.bmi as bmi

def test_bmi_under_weight():
    height = 1.73
    weight = 50

    result = bmi.calculate_bmi(height, weight)

    assert result == -1

def test_bmi_normal_weight() :
    height = 1.73
    weight = 70

    result = bmi.calculate_bmi(height, weight)

    assert result == 0

def test_bmi_over_weight():
    height = 1.73
    weight = 90

    result = bmi.calculate_bmi(height, weight)

    assert result == 1