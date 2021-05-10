from typing import List
import unittest
from string import ascii_lowercase


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(len(s1)):
            s1_map[ascii_lowercase.index(s1[i])] += 1
            s2_map[ascii_lowercase.index(s2[i])] += 1

        for i in range(len(s2) - len(s1)):
            if self.matches(s1_map, s2_map):
                return True

            s2_map[ascii_lowercase.index(s2[i + len(s1)])] += 1
            s2_map[ascii_lowercase.index(s2[i])] -= 1

        return self.matches(s1_map, s2_map)

    def matches(self, s1_map: List[int], s2_map: List[int]):
        for i in range(len(s1_map)):
            if s1_map[i] != s2_map[i]:
                return False

        return True


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.checkInclusion("ky", "ainwkckifykxlribaypk"), True)
        self.assertEqual(s.checkInclusion("adc", "dcda"), True)
        self.assertEqual(s.checkInclusion("hello", "ooolleoooleh"), False)


if __name__ == "__main__":
    unittest.main()
