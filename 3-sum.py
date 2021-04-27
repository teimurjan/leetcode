from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        added_keys = set()

        for i, num in enumerate(nums):
            j, k = self.twoSum(nums, -num)

            if i != j and i != k and k != j:
                result_item = sorted([nums[i], nums[j], nums[k]])
                result_item_key = (
                    str(result_item[0]) +
                    str(result_item[1]) +
                    str(result_item[2])
                )

                if result_item_key not in added_keys:
                  added_keys.add(result_item_key)
                  result.append(result_item)

        return result

    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        index_of_num = {}

        for i, num in enumerate(nums):
            index_of_num[num] = i

        for i, num in enumerate(nums):
            contender_index = index_of_num.get(target - num)
            if index_of_num.get(target - num) and i != contender_index:
                return i, contender_index

        return 0, 0


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.threeSum(
            [-1, 0, 1, 2, -1, -4]),
            [[-1, -1, 2], [-1, 0, 1]]
        )


if __name__ == '__main__':
    unittest.main()
