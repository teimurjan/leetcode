from typing import List
import unittest


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[0:m]
        i, j, k = 0, 0, 0

        while i < m + n:
            if j >= n or (k < m and nums1_copy[k] < nums2[j]):
                nums1[i] = nums1_copy[k]
                k += 1
            else:
                nums1[i] = nums2[j]
                j += 1

            i += 1


class Test(unittest.TestCase):
    def test_1(self):
        s = Solution()

        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3

        s.merge(nums1, m, nums2, n)

        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_2(self):
        s = Solution()

        nums1 = [1]
        m = 1
        nums2 = []
        n = 0

        s.merge(nums1, m, nums2, n)

        self.assertEqual(nums1, [1])

    def test_3(self):
        s = Solution()

        nums1 = [4, 0, 0, 0, 0, 0]
        m = 1
        nums2 = [1, 2, 3, 5, 6]
        n = 5

        s.merge(nums1, m, nums2, n)

        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_4(self):
        s = Solution()

        nums1 = [1, 2, 4, 5, 6, 0]
        m = 5
        nums2 = [3]
        n = 1

        s.merge(nums1, m, nums2, n)

        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
