import unittest
from main import calculate_average

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        result = calculate_average([1, 2, 3])
        self.assertEqual(result, 2.0)

    def test_negative_numbers(self):
        result = calculate_average([-3, -2, -1])
        self.assertEqual(result, -2.0)

    def test_mixed_numbers(self):
        result = calculate_average([-1, 0, 1])
        self.assertEqual(result, 0.0)

    def test_empty_list(self):
        result = calculate_average([])
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()