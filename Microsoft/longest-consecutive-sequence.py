# https://leetcode.com/problems/longest-consecutive-sequence/submissions/2066945296/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for i in s:
            if i-1 not in s:
                count = 1
                print(i)
                while i+1 in s:
                    i += 1
                    count += 1
                ans = max(ans, count)
                print(ans)
        return ans