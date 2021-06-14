from typing import Optional
import unittest
import math


class Solution:
    def numSquares(self, n: int) -> float:
        nearest_square = int(math.sqrt(n)) + 1
        square_nums = [i ** 2 for i in range(0, nearest_square)]
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.numSquares(13), 2)
        self.assertEqual(s.numSquares(12), 3)


if __name__ == "__main__":
    unittest.main()
