# https://leetcode.com/problems/search-a-2d-matrix/submissions/2062690457/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Flatten + Binary Search
# The matrix is sorted row-by-row and each row's first element is greater than
# the previous row's last element — so flattening it yields a fully sorted array.
# Standard binary search on the flattened array finds the target in O(log(m*n)).
# Time: O(m*n) for flattening, O(log(m*n)) for search  Space: O(m*n)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten the 2D matrix into a sorted 1D array
        arr = []
        for i in matrix:
            arr += i

        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            if arr[mid] > target:
                r = mid - 1   # target is in the left half
            else:
                l = mid + 1   # target is in the right half
        return False



# optimal
# https://leetcode.com/problems/search-a-2d-matrix/submissions/2062701692/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        def func(m,n):
            for row in range(1,m+1):
                for col in range(1,n+1):
                    if row == 1 or col == 1:
                        dp[row][col] = 1
                    else:
                        dp[row][col] = dp[row][col-1]+ dp[row-1][col]
            return dp[m][n]
        return func(m,n)