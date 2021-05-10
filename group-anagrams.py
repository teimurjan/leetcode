from typing import List
import unittest


class Solution:
    def serializeStr(self, str: str):
        return tuple(sorted(str))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str_ in strs:
            serialized = self.serializeStr(str_)
            if seen.get(serialized) is None:
                seen[serialized] = 1
            else:
                seen[serialized] += 1

        groups = {}
        for str_ in strs:
            serialized = self.serializeStr(str_)
            if seen[serialized]:
                seen[serialized] -= 1
                if groups.get(serialized):
                    groups[serialized].append(str_)
                else:
                    groups[serialized] = [str_]

        return list(groups.values())


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(
            s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        )
        self.assertEqual(s.groupAnagrams([""]), [[""]])
        self.assertEqual(s.groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()
