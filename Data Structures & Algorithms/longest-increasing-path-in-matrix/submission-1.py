class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        def dfs(r, c, prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] <= prev:
                return 0
            if dp[r][c]:
                return dp[r][c]

            val = matrix[r][c]
            up = dfs(r - 1, c, val)
            down = dfs(r + 1, c, val)
            left = dfs(r, c - 1, val)
            right = dfs(r, c + 1, val)

            dp[r][c] = 1 + max(up, down, left, right)
            return dp[r][c]

        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r, c, -1))
        return res