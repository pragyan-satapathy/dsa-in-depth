# Approach: Precompute suffix maximum
# For each day i, the best we can do if we buy on day i is to sell on the day
# with the highest price AFTER i. So precompute suffixMax[i] = max(prices[i:]).
# Then sweep left-to-right: profit at i = suffixMax[i+1] - prices[i].
# Time: O(n)  Space: O(n)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Build suffix-max array from right to left.
        # localMax[j] (before reversal) stores the running max from the right end up to index j.
        localMax = [prices[-1]]
        for i in range(len(prices) - 2, -1, -1):
            if localMax[-1] < prices[i]:
                localMax.append(prices[i])   # current price is a new right-side max
            else:
                localMax.append(localMax[-1])  # carry forward the previous max
        localMax = localMax[::-1]  # reverse so localMax[i] = max(prices[i:])

        res = 0
        for i in range(len(prices) - 1):
            # Best profit buying on day i: sell on the day with max price after i
            res = max(localMax[i + 1] - prices[i], res)
        return res