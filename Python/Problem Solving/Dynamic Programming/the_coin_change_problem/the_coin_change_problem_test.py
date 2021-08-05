import unittest
from the_coin_change_problem_v1 import getWays


class CoinChangeTest(unittest.TestCase):
    def test_coin_change_4(self):
        self.assertEqual(getWays(4, [1, 2, 3]), 4)

    def test_coin_change_5(self):
        self.assertEqual(getWays(5, [1, 2, 3]), 5)

    def test_coin_change_10(self):
        self.assertEqual(getWays(10, [2, 5, 3, 6]), 5)

    def test_coin_change_0(self):
        self.assertEqual(getWays(0, [2, 5, 8]), 1)


if __name__ == "__main__":
    unittest.main()
