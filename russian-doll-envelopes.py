from typing import List
import unittest


# Time limit exceeded. Use LIS with binary search to fight it
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))

        dp = [1] * len(envelopes)

        global_max = 1
        for i in range(len(envelopes)):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    local_max = max(dp[i], dp[j] + 1)
                    dp[i] = local_max
                    global_max = max(global_max, local_max)

        return global_max


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]), 3)
        self.assertEqual(s.maxEnvelopes([[1, 1], [1, 1], [1, 1]]), 1)
        self.assertEqual(s.maxEnvelopes([[4, 5], [6, 7], [2, 3]]), 3)


if __name__ == "__main__":
    unittest.main()
