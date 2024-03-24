"""Тесты unittest для класса Rectangle"""

import unittest

from rectangle import InvalidSizeError, Rectangle


class TestRectangle(unittest.TestCase):

    def test_valid_values(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle._length, 5)
        self.assertEqual(rectangle._width, 3)

    def test_square_rectangle(self):
        rectangle = Rectangle(4)
        self.assertEqual(rectangle._length, 4)

    def test_negative_length(self):
        with self.assertRaises(InvalidSizeError):
            rectangle = Rectangle(-5, 3)

    def test_negative_width(self):
        with self.assertRaises(InvalidSizeError):
            rectangle = Rectangle(5, -3)

    def test_zero_length(self):
        with self.assertRaises(InvalidSizeError):
            rectangle = Rectangle(0, 3)

    def test_zero_width(self):
        with self.assertRaises(InvalidSizeError):
            rectangle = Rectangle(5, 0)

    def test_invalid_rectangle(self):
        with self.assertRaises(InvalidSizeError):
            rectangle = Rectangle(0, 0)

    def test_addition(self):
        rectangle1 = Rectangle(8, 5)
        rectangle2 = Rectangle(4, 3)
        result = rectangle1 + rectangle2
        self.assertEqual(result.length, 10)
        self.assertEqual(result.width, 10)

    def test_subtraction(self):
        rectangle1 = Rectangle(8, 5)
        rectangle2 = Rectangle(4, 3)
        result = rectangle1 - rectangle2
        self.assertEqual(result.length, 3)
        self.assertEqual(result.width, 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)
