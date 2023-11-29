import unittest
from src.data_capture import DataCapture


class TestDataCapture(unittest.TestCase):
    def test_add_valid_numbers(self):
        capture = DataCapture()

        for number in [3, 9, 3, 4, 6]:
            capture.add(number)

        self.assertEqual(capture.data[3], 2)  # There are two 3s added
        self.assertEqual(capture.data[9], 1)  # There is one 9 added

    def test_add_invalid_numbers(self):
        capture = DataCapture()

        with self.assertRaises(ValueError):
            capture.add(-1)  # Negative numbers are not allowed

        with self.assertRaises(ValueError):
            capture.add(capture.SIZE)  # Numbers greater than a fixed

    def test_less_method(self):
        capture = DataCapture()

        for number in [3, 9, 3, 4, 6]:
            capture.add(number)

        stats = capture.build_stats()
        self.assertEqual(stats.less(4), 2)  # Only two numbers (3, 3) are less than 4

    def test_greater_method(self):
        capture = DataCapture()

        for number in [3, 9, 3, 4, 6]:
            capture.add(number)

        stats = capture.build_stats()
        self.assertEqual(
            stats.greater(4), 2
        )  # Only two numbers (6, 9) are greater than 4

    def test_between_method(self):
        capture = DataCapture()

        for number in [3, 9, 3, 4, 6]:
            capture.add(number)

        stats = capture.build_stats()
        self.assertEqual(
            stats.between(3, 6), 4
        )  # Four numbers (3, 3, 4, 6) are between 3 and 6


if __name__ == "__main__":
    unittest.main()
