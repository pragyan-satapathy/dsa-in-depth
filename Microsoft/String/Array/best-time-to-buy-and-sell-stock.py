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



# Optimal Approach: Track running minimum (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days)
# Instead of precomputing a suffix-max array, just track the lowest price seen
# so far as we scan left-to-right. At each day, the best profit if we sell today
# is (today's price - lowest price seen before today).
# Time: O(n)  Space: O(1)
# ============
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        localMin = prices[0]  # cheapest buy price seen so far
        res = 0
        for i in prices:
            localMin = min(localMin, i)      # update cheapest buy price
            res = max(res, i - localMin)     # best profit if we sell today
        return res