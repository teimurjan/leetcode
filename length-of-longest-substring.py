import unittest


class SlidingWindowSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        left, right = 0, 0

        visited = set()

        while right < len(s):
            if s[right] in visited:
                result = max(result, len(visited))

                while s[right] in visited:
                    visited.remove(s[left])
                    left += 1
            else:
                visited.add(s[right])
                right += 1

        result = max(result, len(visited))

        return result


class SlidingWindowOptimizedSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        left, right = 0, 0

        visited = {}

        while right < len(s):
            is_visited = visited.get(s[right]) is not None
            if is_visited:
                result = max(result, right - left)
                next_after_visited_index = visited[s[right]] + 1
                left = (
                    next_after_visited_index
                    if left < next_after_visited_index
                    else left
                )

            visited[s[right]] = right
            right += 1

        result = max(result, right - left)

        return result


class Test(unittest.TestCase):
    def test_sliding_window(self):
        s = SlidingWindowSolution()

        self.assertEqual(s.lengthOfLongestSubstring("tmmzuxt"), 5)
        self.assertEqual(s.lengthOfLongestSubstring("abba"), 2)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("dvdf"), 3)

    def test_sliding_window_optimized(self):
        s = SlidingWindowOptimizedSolution()

        self.assertEqual(s.lengthOfLongestSubstring("tmmzuxt"), 5)
        self.assertEqual(s.lengthOfLongestSubstring("abba"), 2)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("dvdf"), 3)


if __name__ == "__main__":
    unittest.main()
