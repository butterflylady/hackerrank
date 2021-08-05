import unittest
from the_maximum_subarray import maxSubarray


class maxSubarrayTest(unittest.TestCase):
    def test_subarray_only_positive(self):
        self.assertEqual(maxSubarray([1, 2, 3, 4]), (10, 10))

    def test_subarray_only_negative(self):
        self.assertEqual(maxSubarray([-2, -3, -1, -4, -6]), (-1, -1))

    def test_subarray(self):
        self.assertEqual(maxSubarray([2, -1, 2, 3, 4, -5]), (10, 11))
