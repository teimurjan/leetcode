from typing import List
import unittest


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if left_max < height[left]:
                    left_max = height[left]
                else:
                    water += left_max - height[left]

                left += 1
            else:
                if right_max < height[right]:
                    right_max = height[right]
                else:
                    water += right_max - height[right]

                right -= 1
        
        return water


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)


if __name__ == "__main__":
    unittest.main()
