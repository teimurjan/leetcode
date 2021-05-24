from typing import List
import unittest


class Solution:
    def __init__(self):
        self.letter_mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def getCombination(self, digits: str):
        if len(digits) == 0:
            return []

        if len(digits) == 1:
            return self.letter_mapping[digits[0]]

        result = []
        for letter in self.letter_mapping[digits[0]]:
            for next_letter in self.getCombination(digits[1:]):
                result.append(letter + next_letter)

        return result

    def letterCombinations(self, digits: str) -> List[str]:
        return self.getCombination(digits)


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(
            s.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )
        self.assertEqual(
            s.letterCombinations(""),
            [],
        )


if __name__ == "__main__":
    unittest.main()
