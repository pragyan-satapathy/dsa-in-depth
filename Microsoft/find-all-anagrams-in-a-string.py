# https://leetcode.com/problems/find-all-anagrams-in-a-string/submissions/2064722279/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

class Solution:
    from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter()
        res = []
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1
            if right - left + 1 > len(p):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            if window == p_count:
                res.append(left)

        return res