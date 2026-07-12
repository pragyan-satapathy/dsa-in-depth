# https://leetcode.com/problems/count-subarrays-with-majority-element-i/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/count-subarrays-with-majority-element-i/submissions/2063589182/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            cont = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    cont += 1
                if cont*2 > j-i+1:
                    res += 1
        return res