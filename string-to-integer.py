import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        max_result = 2147483647
        min_result = -2147483648
        result = ''

        i = 0

        while i < len(s) and s[i] == ' ':
            i += 1

        sign = '+'
        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            sign = s[i]
            i += 1

        while i < len(s) and s[i].isnumeric():
            result += s[i]
            i += 1

        if not result:
            return 0

        result = int(sign + result)

        return min(result, max_result) if result >= 0 else max(result, min_result)


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.myAtoi('+-12'), 0)
        self.assertEqual(s.myAtoi('    -42'), -42)
        self.assertEqual(s.myAtoi('42'), 42)
        self.assertEqual(s.myAtoi('4193 with words'), 4193)
        self.assertEqual(s.myAtoi('words and 987'), 0)
        self.assertEqual(s.myAtoi('-91283472332'), -2147483648)
        self.assertEqual(s.myAtoi('91283472332'), 2147483647)


if __name__ == '__main__':
    unittest.main()
