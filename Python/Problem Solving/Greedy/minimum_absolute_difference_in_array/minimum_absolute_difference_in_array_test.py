import unittest
from minimum_absolute_difference_in_array import minimumAbsoluteDifference


class MinAbsDiffArrTest(unittest.TestCase):
    def test_min_abs_diff_arr_1(self):
        self.assertEqual(minimumAbsoluteDifference([3, -7, 0]), 3)

    def test_min_abs_diff_arr_2(self):
        self.assertEqual(minimumAbsoluteDifference([1, -3, 71, 68, 17]), 3)

    def test_min_abs_diff_arr_3(self):
        self.assertEqual(minimumAbsoluteDifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]), 1)


if __name__ == '__main__':
    unittest.main()
