from typing import List
import unittest


class SolutionMerge:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []

        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1

        while i < len(nums1):
            nums.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums.append(nums2[j])
            j += 1

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        half_len = len(nums) // 2
        if len(nums) % 2 == 0:
            return (nums[half_len - 1] + nums[half_len]) / 2

        return nums[half_len]


class SolutionBinary:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        lo, hi = 0, len(nums1)
        combined_len = len(nums1) + len(nums2)

        while lo <= hi:
            partition_x = (lo + hi) // 2
            partition_y = (combined_len + 1) // 2 - partition_x

            left_x = nums1[partition_x - 1] if partition_x > 0 else float("-inf")
            right_x = (
                nums1[partition_x + 1] if partition_x < len(nums1) - 1 else float("inf")
            )

            left_y = nums2[partition_y - 1] if partition_y > 0 else float("-inf")
            right_y = (
                nums2[partition_y + 1] if partition_y < len(nums2) - 1 else float("inf")
            )

            if left_x <= right_y and left_y <= right_x:
                return (
                    max(left_x, left_y)
                    if combined_len % 2 != 0
                    else (max(left_x, left_y) + min(right_x, right_y)) / 2
                )

            if left_x > right_y:
                hi = partition_x - 1
            if left_y > right_x:
                lo = partition_x + 1

        return -1


class Test(unittest.TestCase):
    def test_merge(self):
        s = SolutionMerge()

        self.assertEqual(s.findMedianSortedArrays([1, 3], [2]), 2)
        self.assertEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(s.findMedianSortedArrays([0, 0], [0, 0]), 0)
        self.assertEqual(s.findMedianSortedArrays([], [1]), 1)
        self.assertEqual(s.findMedianSortedArrays([2], []), 2)

    def test_binary(self):
        s = SolutionBinary()

        self.assertEqual(s.findMedianSortedArrays([1, 3], [2]), 2)
        self.assertEqual(s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)
        self.assertEqual(s.findMedianSortedArrays([0, 0], [0, 0]), 0)
        self.assertEqual(s.findMedianSortedArrays([], [1]), 1)
        self.assertEqual(s.findMedianSortedArrays([2], []), 2)


if __name__ == "__main__":
    unittest.main()
