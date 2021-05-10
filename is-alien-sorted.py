from typing import List


import unittest


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index_of = {}

        for i, char in enumerate(order):
            index_of[char] = i

        max_word_len = 0
        for word in words:
            max_word_len = max(max_word_len, len(word))

        j = 0
        while j < max_word_len:
            prev_weight = -1
            duplicates = 0

            for word in words:
                if j > len(word) - 1:
                    weight = -1
                else:
                    weight = index_of[word[j]]

                if prev_weight > weight:
                    return False
                elif prev_weight == weight:
                    duplicates += 1

                prev_weight = weight

            if duplicates == 0:
                return True

            j += 1

        return True


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(
            s.isAlienSorted(["app", "apple"], "abcdefghijklmnopqrstuvwxyz"), True
        )


if __name__ == "__main__":
    unittest.main()
