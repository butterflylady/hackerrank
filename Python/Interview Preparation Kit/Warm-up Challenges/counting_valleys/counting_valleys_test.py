import unittest
from counting_valleys import counting_valleys


class CountingValleyTest(unittest.TestCase):
    def test_no_valley_case_1(self):
        self.assertEqual(counting_valleys(1, "U"), 0)

    def test_no_valley_case_2(self):
        self.assertEqual(counting_valleys(3, "DDD"), 0)

    def test_no_valley_case_3(self):
        self.assertEqual(counting_valleys(3, "UUU"), 0)

    def test_one_valley(self):
        self.assertEqual(counting_valleys(8, "UDDDUDUU"), 1)

    def test_two_valleys(self):
        self.assertEqual(counting_valleys(8, "UUDDDDUDUUDU"), 2)


if __name__ == "__main__":
    unittest.main()
