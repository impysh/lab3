import Lab3

print("Test_Lab3")

# The “assert” statement basically returns a Boolean value True or False of the
# condition asserted or checked is True or False.

def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_large_input():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 50, 70, 80, 100]  # Input with 11 numbers

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 1
def test_bubble_sort_empty_input():
    input_arr = []  # Empty input list

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 0

def test_bubble_sort_non_integer_input():
    input_arr = [64, 34, 25, 12, "22", 11, 90]  # Input with a non-integer value ("22")

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert result == 2

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])