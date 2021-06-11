from typing import Tuple
import unittest


class Solution:
    def calculateHelper(self, s: str, i: int) -> Tuple[int, int]:
        result = 0
        sign = ""

        while i < len(s) and s[i] != ")":
            if s[i] == "(":
                expr, i = self.calculateHelper(s, i + 1)
                result += expr * int(sign + "1")
                sign = ""
            elif s[i].isdigit():
                digit = ""
                while i < len(s) and s[i].isdigit():
                    digit += s[i]
                    i += 1
                result += int(sign + digit)
                sign = ""
            elif s[i] == "-" or s[i] == "+":
                if sign == "-" and s[i] == "-":
                    sign = "+"
                elif sign == "-" and s[i] == "+":
                    sign = "-"
                else:
                    sign = s[i]
                i += 1
            else:
                i += 1

        return result, i + 1

    def calculate(self, s: str) -> int:
        return self.calculateHelper(s, 0)[0]


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.calculate("(7)-(0)+(4)"), 11)
        self.assertEqual(s.calculate(" 2-1 + 2 "), 3)
        self.assertEqual(s.calculate("(1+(4+5+2)-3)+(6+8)"), 23)
        self.assertEqual(s.calculate("1 + 1"), 2)
        self.assertEqual(s.calculate("+48 + -48"), 0)
        self.assertEqual(s.calculate("- (3 + (4 + 5))"), -12)
        self.assertEqual(s.calculate("1-(+1+1)"), -1)
        


if __name__ == "__main__":
    unittest.main()
