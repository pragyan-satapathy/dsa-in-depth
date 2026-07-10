# https://leetcode.com/problems/maximum-subarray/submissions/2062529189/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Kadane's Algorithm (DP)
# arr[i] = maximum subarray sum ending at index i.
# At each position we choose: start a new subarray at i, or extend the previous one.
#   arr[i] = max(nums[i], nums[i] + arr[i-1])
# If the running sum so far is negative, it only drags us down — better to start fresh.
# The answer is the maximum value across all arr[i].
# Time: O(n)  Space: O(n)  (can be reduced to O(1) by keeping only the last value)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr = [nums[0]]   # arr[i] = max subarray sum ending at i
        res = nums[0]     # global maximum seen so far
        for i in range(1, len(nums)):
            # extend previous subarray if it improves the sum, otherwise start fresh
            a = max(nums[i], nums[i] + arr[-1])
            arr.append(a)
            res = max(res, a)
        return res
        