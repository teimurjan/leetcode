from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        low, high = 0, len(nums) - 1

        while low < high:
            sum_ = nums[low] + nums[high]
            if sum_ == target:
                return [low + 1, high + 1]

            if sum_ < target:
                low += 1
            else:
                high -= 1

        return [0, 0]


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [1, 2])


if __name__ == '__main__':
    unittest.main()
