from typing import List
import unittest


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i <= 0:
            nums.reverse()
            return

        j = len(nums) - 1
        while nums[j] <= nums[i - 1] and j >= 0:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        nums_1 = [3, 2, 1]
        nums_1_final = [1, 2, 3]

        nums_2 = [4, 5, 6]
        nums_2_final = [4, 6, 5]

        nums_3 = [1]
        nums_3_final = [1]

        nums_4 = []
        nums_4_final = []

        nums_5 = [2, 3]
        nums_5_final = [3, 2]

        nums_6 = [1, 5, 8, 4, 7, 6, 5, 3, 1]
        nums_6_final = [1, 5, 8, 5, 1, 3, 4, 6, 7]

        s.nextPermutation(nums_1)
        self.assertEqual(nums_1, nums_1_final)

        s.nextPermutation(nums_2)
        self.assertEqual(nums_2, nums_2_final)

        s.nextPermutation(nums_3)
        self.assertEqual(nums_3, nums_3_final)

        s.nextPermutation(nums_4)
        self.assertEqual(nums_4, nums_4_final)

        s.nextPermutation(nums_5)
        self.assertEqual(nums_5, nums_5_final)

        s.nextPermutation(nums_6)
        self.assertEqual(nums_6, nums_6_final)


if __name__ == "__main__":
    unittest.main()
