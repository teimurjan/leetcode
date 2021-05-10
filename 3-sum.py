from typing import List, Set
import unittest


class SolutionTwoSum:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        prev = None
        for i, num in enumerate(nums):
            if num > 0:
                break
            if num == prev:
                continue

            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)

        return result

    def twoSum(self, nums: List[int], pos: int, result: List[List[int]]):
        seen = set()
        j = pos + 1

        while j < len(nums):
            contender = -nums[pos] - nums[j]
            if contender in seen:
                result.append([nums[pos], nums[j], contender])

                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1

            seen.add(nums[j])
            j += 1


class SolutionTwoSum2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        prev = None
        for i, num in enumerate(nums):
            if num > 0:
                break
            if num == prev:
                continue

            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, result)

        return result

    def twoSum(self, nums: List[int], pos: int, result: List[List[int]]):
        low, high = pos + 1, len(nums) - 1

        while low < high:
            sum_ = nums[pos] + nums[low] + nums[high]
            if sum_ == 0:
                result.append([nums[pos], nums[low], nums[high]])

                low += 1
                high -= 1

                # skip duplicates
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
            elif sum_ < 0:
                low += 1
            else:
                high -= 1


class SolutionNoSort:
    def threeSum(self, nums: List[int]) -> Set[List[int]]:
        result = set()
        duplicates = set()
        seen = {}

        for i, num in enumerate(nums):
            if num in duplicates:
                continue

            for j in range(i + 1, len(nums)):
                duplicates.add(num)
                num_j = nums[j]
                complement = -num - num_j

                if complement in seen and seen[complement] == i:
                    result.add(tuple(sorted([num, num_j, complement])))

                seen[num_j] = i

        return result


class Test(unittest.TestCase):
    def test_solution_two_sum(self):
        s = SolutionTwoSum()

        self.assertEqual(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 1, 0], [-1, 2, -1]])

    def test_solution_two_sum_2(self):
        s = SolutionTwoSum2()

        self.assertEqual(s.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_solution_no_sort(self):
        s = SolutionNoSort()

        self.assertEqual(
            s.threeSum([-1, 0, 1, 2, -1, -4]), set([(-1, -1, 2), (-1, 0, 1)])
        )


if __name__ == "__main__":
    unittest.main()
