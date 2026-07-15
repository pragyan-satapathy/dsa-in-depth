# https://leetcode.com/problems/pascals-triangle/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/pascals-triangle/submissions/2066924044/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Build row by row
# Each row starts and ends with 1. Every interior element equals the sum of the
# two elements directly above it from the previous row: prev[i] + prev[i+1].
# Time: O(n²)  Space: O(n²)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]   # first row is always [1]
        for _ in range(1, numRows):
            row = [1]        # every row starts with 1
            prev = res[-1]   # the row directly above
            for i in range(len(prev) - 1):
                row.append(prev[i] + prev[i+1])   # interior elements: sum of two parents
            row.append(1)    # every row ends with 1 (prev[-1] is always 1 but explicit here)
            res.append(row)
        return res