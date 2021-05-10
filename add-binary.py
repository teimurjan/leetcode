import unittest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""

        i, j = len(a) - 1, len(b) - 1

        carry = 0
        while i >= 0 or j >= 0:
            a_i = int(a[i]) if i >= 0 else 0
            b_j = int(b[j]) if j >= 0 else 0

            sum_ = a_i + b_j + carry
            carry = 0 if sum_ < 2 else 1
            result = str(sum_ % 2) + result

            i -= 1
            j -= 1

        if carry:
            result = "1" + result

        return result


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(s.addBinary("1111", "1111"), "11110")
        self.assertEqual(s.addBinary("1010", "1011"), "10101")
        self.assertEqual(s.addBinary("11", "1"), "100")


if __name__ == "__main__":
    unittest.main()
