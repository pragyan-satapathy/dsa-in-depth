# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/submissions/2065674513/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        while j<= len(haystack) - len(needle):
            for i in range(len(needle)):
                if haystack[i+j] != needle[i]:
                    j = j+1
                    break
            else:
                return j
        return -1