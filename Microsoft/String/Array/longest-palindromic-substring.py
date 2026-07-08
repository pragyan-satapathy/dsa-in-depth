# https://leetcode.com/problems/longest-palindromic-substring/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Expand Around Center
# For each character (and each gap between characters), try to expand outward
# as long as the characters on both sides match.
# - Odd-length palindromes: center is a single character → expand(i, i)
# - Even-length palindromes: center is between two characters → expand(i, i+1)
# Track the longest palindrome seen so far via start/end indices.
# Time: O(n²)  Space: O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def expand(l, r):
            # Expand outward while characters match and indices are in bounds.
            # When the loop exits, l and r have gone one step too far,
            # so the valid palindrome window is [l+1, r-1].
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)       # odd-length: single char center
            l2, r2 = expand(i, i + 1)   # even-length: gap between i and i+1

            if (r1 - l1) > (end - start):
                start, end = l1, r1
            if (r2 - l2) > (end - start):
                start, end = l2, r2

        return s[start: end + 1]
            
