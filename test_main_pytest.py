from main import calculate_average

def test_positive_numbers():
    result = calculate_average([1, 2, 3])
    assert result == 2.0

def test_negative_numbers():
    result = calculate_average([-3, -2, -1])
    assert result == -2.0

def test_mixed_numbers():
    result = calculate_average([-1, 0, 1])
    assert result == 0.0

def test_empty_list():
    result = calculate_average([])
    assert result is None