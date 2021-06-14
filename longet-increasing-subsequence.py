from typing import List
import unittest


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        max_overall = 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    max_overall = max(max_overall, dp[i])
         

        return max_overall


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.lengthOfLIS([-1, 3, 4, 5, 2, 2, 2, 2]), 4)
        self.assertEqual(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)


if __name__ == "__main__":
    unittest.main()
