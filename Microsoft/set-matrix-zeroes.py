# https://leetcode.com/problems/set-matrix-zeroes/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/set-matrix-zeroes/submissions/2068313691/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Two-pass with row/col sets
# We can't zero out rows/columns on the first pass because that would create new
# zeros, causing incorrect propagation. Instead:
#   Pass 1 — record which rows and columns contain a zero.
#   Pass 2 — zero out any cell whose row or column was recorded.
# Time: O(m*n)  Space: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()   # rows that contain at least one zero
        col = set()   # columns that contain at least one zero

        # pass 1: collect rows and columns that need to be zeroed
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        # pass 2: zero out cells belonging to a marked row or column
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row or j in col:
                    matrix[i][j] = 0