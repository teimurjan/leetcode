from typing import Tuple
import unittest
import time


def memo(fn):
    seen = {}

    def memoized(*args):
        if args in seen:
            return seen[args]

        result = fn(*args)
        seen[args] = result

        return result

    return memoized


class SolutionBruteForce:
    def longestPalindromeHelper(
        self, start: int, end: int, s: str
    ) -> Tuple[int, int, int]:
        if start > end:
            return 0, start, end

        if start == end:
            return 1, start, end

        if s[start] == s[end]:
            desired_length = end - start - 1
            inner_length, _, _ = self.longestPalindromeHelper(start + 1, end - 1, s)
            if desired_length == inner_length:
                return desired_length + 2, start, end

        length1, start1, end1 = self.longestPalindromeHelper(start, end - 1, s)
        length2, start2, end2 = self.longestPalindromeHelper(start + 1, end, s)

        if length1 > length2:
            return length1, start1, end1

        return length2, start2, end2

    def longestPalindrome(self, s: str) -> str:
        _, start, end = self.longestPalindromeHelper(0, len(s) - 1, s)
        return s[start : end + 1]


class SolutionMemoized(SolutionBruteForce):
    @memo
    def longestPalindromeHelper(
        self, start: int, end: int, s: str
    ) -> Tuple[int, int, int]:
        if start > end:
            return 0, start, end

        if start == end:
            return 1, start, end

        if s[start] == s[end]:
            desired_length = end - start - 1
            inner_length, _, _ = self.longestPalindromeHelper(start + 1, end - 1, s)
            if desired_length == inner_length:
                return desired_length + 2, start, end

        length1, start1, end1 = self.longestPalindromeHelper(start, end - 1, s)
        length2, start2, end2 = self.longestPalindromeHelper(start + 1, end, s)

        if length1 > length2:
            return length1, start1, end1

        return length2, start2, end2

    def longestPalindrome(self, s: str) -> str:
        _, start, end = self.longestPalindromeHelper(0, len(s) - 1, s)
        return s[start : end + 1]


class Test(unittest.TestCase):
    def test_brute_force(self):
        s = SolutionBruteForce()

        start_time = time.time()
        self.assertIn(s.longestPalindrome("babad"), ["bab", "aba"])
        self.assertEqual(s.longestPalindrome("cbbd"), "bb")
        self.assertEqual(s.longestPalindrome("a"), "a")
        self.assertIn(s.longestPalindrome("ac"), ["a", "c"])
        self.assertEqual(s.longestPalindrome("aacabdkacaa"), "aca")
        print(f"\nBRUTE FORCE: {time.time() - start_time} seconds")

    def test_solution_memo(self):
        s = SolutionMemoized()

        start_time = time.time()
        self.assertIn(s.longestPalindrome("babad"), ["bab", "aba"])
        self.assertEqual(s.longestPalindrome("cbbd"), "bb")
        self.assertEqual(s.longestPalindrome("a"), "a")
        self.assertIn(s.longestPalindrome("ac"), ["a", "c"])
        self.assertEqual(s.longestPalindrome("aacabdkacaa"), "aca")
        print(f"\nMEMO: {time.time() - start_time} seconds")


if __name__ == "__main__":
    unittest.main()
