from typing import List
import unittest


class Solution:
    def bfs(self, x: int, y: int, m: int, n: int, grid: List[List[str]]):
        if not (n > x >= 0 and y < m and m > y >= 0) or grid[y][x] != "1":
            return

        grid[y][x] = "0"

        self.bfs(x + 1, y, m, n, grid)
        self.bfs(x - 1, y, m, n, grid)
        self.bfs(x, y - 1, m, n, grid)
        self.bfs(x, y + 1, m, n, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0

        num_of_islands = 0

        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if grid[y][x] == "1":
                    num_of_islands += 1
                    self.bfs(x, y, m, n, grid)

        return num_of_islands


class Test(unittest.TestCase):
    def test(self):
        s = Solution()

        self.assertEqual(
            s.numIslands([["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]),
            1,
        )
        self.assertEqual(
            s.numIslands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )
        self.assertEqual(
            s.numIslands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main()
