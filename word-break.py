from typing import FrozenSet, List
import unittest


def memo(fn):
    seen = {}

    def memoized(*args):
        if args in seen:
            return seen[args]

        result = fn(*args)
        seen[args] = result

        return result

    return memoized


class Solution:
    @memo
    def wordBreakHelper(self, s: str, words_set: FrozenSet[str], start: int) -> bool:
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in words_set and self.wordBreakHelper(s, words_set, end):
                return True

        return False

    def wordBreak(self, s: str, words: List[str]) -> bool:
        return self.wordBreakHelper(s, frozenset(words), 0)


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.wordBreak("aaaaaaa", ["aaaa", "aaa"]), True)
        self.assertEqual(s.wordBreak("leetcode", ["leet", "code"]), True)
        self.assertEqual(s.wordBreak("applepenapple", ["apple", "pen"]), True)
        self.assertEqual(
            s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]), False
        )


if __name__ == "__main__":
    unittest.main()
