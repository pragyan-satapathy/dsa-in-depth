# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/2063558532/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Sliding window (two pointers)
# Maintain a window [i, j) whose characters are all unique (tracked in set d).
# Expand j when s[j] is not in the window.
# On a duplicate, record the current window length, then shrink from the left
# (increment i, removing s[i] from d) until the duplicate is evicted.
# After the loop, do a final check in case the longest window ends at the last char.
# Time: O(n)  Space: O(min(n, alphabet_size))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()   # characters currently in the window [i, j)
        i, j = 0, 0
        l = 0       # longest valid window seen so far
        while j < len(s):
            if s[j] not in d:
                d.add(s[j])   # expand the window
                j += 1
            else:
                l = max(l, j - i)       # record length before shrinking
                while s[j] in d:        # shrink from the left until duplicate is gone
                    d.remove(s[i])
                    i += 1
        l = max(l, j - i)   # final window may be the longest (no trailing duplicate)
        return l