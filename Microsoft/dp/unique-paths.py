# https://leetcode.com/problems/unique-paths/submissions/2062663636/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Top-down DP (memoization)
# From any cell (m, n) the robot can only move left (m, n-1) or up (m-1, n).
# So: paths(m, n) = paths(m-1, n) + paths(m, n-1)
# Base case: any cell on the first row or first column has exactly 1 path.
# We cache results in a 2-D dp table to avoid recomputation.
# Time: O(m*n)  Space: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        def func(m, n):
            if m == 1 or n == 1:   # only one way to reach any edge cell
                dp[m][n] = 1
                return 1
            if dp[m][n]:           # already computed — return cached result
                return dp[m][n]
            if not dp[m-1][n]:     # compute from above if not cached
                dp[m-1][n] = func(m-1, n)
            if not dp[m][n-1]:     # compute from the left if not cached
                dp[m][n-1] = func(m, n-1)
            dp[m][n] = dp[m][n-1] + dp[m-1][n]   # total paths = sum of both directions
            return dp[m][n]

        return func(m, n)

# Approach: Bottom-up DP (tabulation)
# https://leetcode.com/problems/unique-paths/submissions/2062668629/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# Fill the dp table iteratively instead of recursively.
# Base case: every cell in the first row/column has exactly 1 path.
# Recurrence: dp[row][col] = dp[row-1][col] + dp[row][col-1]
# Time: O(m*n)  Space: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        def func(m, n):
            for row in range(1, m + 1):
                for col in range(1, n + 1):
                    if row == 1 or col == 1:   # edge cells have only one path
                        dp[row][col] = 1
                    else:
                        # paths from above + paths from the left
                        dp[row][col] = dp[row][col-1] + dp[row-1][col]
            return dp[m][n]

        return func(m, n)