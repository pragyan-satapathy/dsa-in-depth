# https://leetcode.com/problems/maximum-subarray/submissions/2062529189/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Kadane's Algorithm (DP)
# arr[i] = maximum subarray sum ending at index i.
# At each position we choose: start a new subarray at i, or extend the previous one.
#   arr[i] = max(nums[i], nums[i] + arr[i-1])
# If the running sum so far is negative, it only drags us down — better to start fresh.
# The answer is the maximum value across all arr[i].
# Time: O(n)  Space: O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]   # max subarray sum ending at current index
        res = nums[0]    # global maximum seen so far

        for i in range(1, len(nums)):
            # extend previous subarray if it improves the sum, otherwise start fresh
            curr = max(nums[i], nums[i] + curr)
            res = max(res, curr)

        return res