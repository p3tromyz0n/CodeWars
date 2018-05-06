import unittest
import sum_of_positive


class SumOfPositiveTest(unittest.TestCase):

    def test_positive_sum_long(self):

        self.assertEqual(sum_of_positive.positive_sum_long([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(sum_of_positive.positive_sum_long([1, 2, 3, 4, 5, 6, 0]), 21)
        self.assertEqual(sum_of_positive.positive_sum_long([1, 2, 3, 4, 5, -6]), 15)
        self.assertEqual(sum_of_positive.positive_sum_long([1, -2, 3, 4, 5, -6]), 13)
        self.assertEqual(sum_of_positive.positive_sum_long([1, -2, -3, 4, 5, -6]), 10)
        self.assertEqual(sum_of_positive.positive_sum_long([-1, -2, -3, 4, 5, -6]), 9)
        self.assertEqual(sum_of_positive.positive_sum_long([-1, -2, -3, -4, 5, -6]), 5)
        self.assertEqual(sum_of_positive.positive_sum_long([-1, -2, -3, -4, -5, -6]), 0)
        self.assertEqual(sum_of_positive.positive_sum_long([]), 0)

    def test_positive_sum_short(self):
        self.assertEqual(sum_of_positive.positive_sum_long([1, 2, 3, 4, 5, 6]), 21)
        self.assertEqual(sum_of_positive.positive_sum_long([1, 2, 3, 4, 5, 6, 0]), 21)
        self.assertEqual(sum_of_positive.positive_sum_long([1, 2, 3, 4, 5, -6]), 15)
        self.assertEqual(sum_of_positive.positive_sum_long([1, -2, 3, 4, 5, -6]), 13)
        self.assertEqual(sum_of_positive.positive_sum_long([1, -2, -3, 4, 5, -6]), 10)
        self.assertEqual(sum_of_positive.positive_sum_long([-1, -2, -3, 4, 5, -6]), 9)
        self.assertEqual(sum_of_positive.positive_sum_long([-1, -2, -3, -4, 5, -6]), 5)
        self.assertEqual(sum_of_positive.positive_sum_long([-1, -2, -3, -4, -5, -6]), 0)
        self.assertEqual(sum_of_positive.positive_sum_long([]), 0)


if __name__ == '__main__':
    unittest.main()