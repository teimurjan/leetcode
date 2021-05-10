import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start <= end:
            if not s[start].isalnum():
                start += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1

        return True


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.isPalindrome("A man, a plan, a canal: Panama"), True)
        self.assertEqual(s.isPalindrome("race a car"), False)
        self.assertEqual(s.isPalindrome("ono"), True)
        self.assertEqual(s.isPalindrome("p"), True)
        self.assertEqual(s.isPalindrome("0P"), False)


if __name__ == "__main__":
    unittest.main()
