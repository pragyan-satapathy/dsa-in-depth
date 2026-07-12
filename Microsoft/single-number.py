#  https://leetcode.com/problems/single-number/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/single-number/submissions/2063545645/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            res ^= nums[i]
        return res