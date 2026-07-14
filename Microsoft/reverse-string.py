# https://leetcode.com/problems/reverse-string/submissions/2066133571/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/reverse-string/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while (i<j):
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1