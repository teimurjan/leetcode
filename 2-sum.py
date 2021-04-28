from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        index_of_num = {}

        for i, num in enumerate(nums):
            index_of_num[num] = i

        for i, num in enumerate(nums):
            contender_index = index_of_num.get(target - num)
            if index_of_num.get(target - num) and i != contender_index:
                return [i, contender_index]

        return 0, 0


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])


if __name__ == '__main__':
    unittest.main()
