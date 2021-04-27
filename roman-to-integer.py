import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        value_of = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1,
        }

        result = 0
        i = 0

        local_result = 0
        curr_group = None

        while i < len(s):
            if curr_group is None:
                curr_group = s[i]
                local_result = value_of[curr_group]
            elif value_of[curr_group] == value_of[s[i]]:
                local_result += value_of[curr_group]
            elif value_of[curr_group] > value_of[s[i]]:
                result += local_result
                curr_group = s[i]
                local_result = value_of[curr_group]
            else:
                result += value_of[s[i]] - local_result
                local_result = 0
                curr_group = None

            i += 1

        result += local_result

        return result


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.romanToInt('LVIII'), 58)
        self.assertEqual(s.romanToInt('III'), 3)
        self.assertEqual(s.romanToInt('IV'), 4)
        self.assertEqual(s.romanToInt('IX'), 9)
        self.assertEqual(s.romanToInt('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
