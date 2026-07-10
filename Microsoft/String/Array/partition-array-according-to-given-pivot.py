# https://leetcode.com/problems/partition-array-according-to-given-pivot/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        mid = []
        after = []
        for i in nums:
            if i>pivot:
                after.append(i)
            elif i == pivot:
                mid.append(i)
            else:
                before.append(i)
        return before+mid+after