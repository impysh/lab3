import lab2.lab2 as lab2

# Test find_min_max()
def test_find_min_max():
    # Test with a list of integers
    num_list = [5, 3, 8, 1, 9]
    max_value, min_value = lab2.find_min_max(num_list)

    assert max_value == 9
    assert min_value == 1

# Test calc_average()
def test_calc_average():
    num_list = [5, 3, 8, 1, 9]
    average = lab2.calc_average(num_list)
    assert average == 5.2

# Test calc_median_temperature()
def test_calc_median_temperature():
    num_list = [5, 3, 8, 1, 9]
    median_value = lab2.calc_median_temperature(num_list)
    assert median_value == 5.0

if __name__ == "__main__":
    pytest.main()
