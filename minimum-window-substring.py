import unittest
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        desired = Counter(t)
        found = {}
        matches = 0
        result = ""

        left, right = 0, 0

        while right < len(s):
            if s[right] in desired:
                found_count = found.get(s[right], 0)
                found[s[right]] = found_count + 1

                if found[s[right]] == desired[s[right]]:
                    matches += 1

            while matches == len(desired):
                if result == "" or right - left < len(result):
                    result = s[left : right + 1]

                if s[left] in found:
                    if found[s[left]] > 1:
                        found[s[left]] -= 1
                    else:
                        del found[s[left]]

                    if found.get(s[left], 0) < desired[s[left]]:
                        matches -= 1

                left += 1

            right += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"), "abbbbbcdd")
        self.assertEqual(s.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(s.minWindow("a", "b"), "")
        self.assertEqual(s.minWindow("a", "aa"), "")
        self.assertEqual(s.minWindow("a", "a"), "a")
        self.assertEqual(s.minWindow("aa", "aa"), "aa")


if __name__ == "__main__":
    unittest.main()
