# https://leetcode.com/problems/longest-common-prefix/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/longest-common-prefix/submissions/2063483278/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Shrink against shortest string
# The common prefix can be at most as long as the shortest string.
# Start with the shortest string as the candidate prefix, then compare it
# character-by-character against every other string. On a mismatch at position j,
# shrink the candidate to [:j] and reduce the search length l accordingly.
# Time: O(n * m)  where n = number of strings, m = length of shortest string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # find the shortest string — the prefix cannot exceed its length
        shortestStr = strs[0]
        l = len(strs[0])
        for i in range(1, len(strs)):
            if len(strs[i]) < l:
                l = len(strs[i])
                shortestStr = strs[i]

        res = shortestStr   # start with the full shortest string as candidate
        for i in strs:
            for j in range(l):
                if res[j] != i[j]:
                    # mismatch at j — shrink the prefix and the search window
                    res = shortestStr[:j]
                    l = j
                    break
        return res