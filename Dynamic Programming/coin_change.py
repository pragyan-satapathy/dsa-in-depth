# https://leetcode.com/problems/coin-change/

# # recursion
# # ============
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [[0 for _ in range(len(coins))] for _ in range (amount+1)]
#         def solve(coins, amount,i):
#             if amount == 0:
#                 return 0
#             if i < 0:
#                 return float('inf')
#             if (dp[amount][i]):
#                 return dp[amount][i]
#             if coins[i]>amount:
#                 dp[amount][i] = solve(coins, amount, i-1)
#                 return dp[amount][i]
#             dp[amount][i] = min(1+solve(coins, amount-coins[i], i), solve(coins, amount, i-1))
#             return dp[amount][i]

#         ans = solve(coins, amount,len(coins)-1)
#         return -1 if math.isinf(ans) else ans



# # memoization
# # ======================
# # https://leetcode.com/problems/coin-change/submissions/2045998197/

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [[0 for _ in range(len(coins))] for _ in range (amount+1)]
#         def solve(coins, amount,i):
#             if amount == 0:
#                 return 0
#             if i < 0:
#                 return float('inf')
#             if (dp[amount][i]):
#                 return dp[amount][i]
#             if coins[i]>amount:
#                 dp[amount][i] = solve(coins, amount, i-1)
#                 return dp[amount][i]
#             dp[amount][i] = min(1+solve(coins, amount-coins[i], i), solve(coins, amount, i-1))
#             return dp[amount][i]

#         ans = solve(coins, amount,len(coins)-1)
#         return -1 if math.isinf(ans) else ans


# dp
# ============================
# https://leetcode.com/problems/coin-change/submissions/2046025638/
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float('inf') for _ in range(len(coins))] for _ in range (amount+1)]
        def solve(coins, amount,i):
            # if amount == 0:
            #     return 0
            for j in range(len(coins)):
                dp[0][j] = 0
            for row in range(1, amount+1):
                for col in range(i+1):   
                    if coins[col] > row:
                        dp[row][col] = dp[row][col-1]
                    else:
                        if dp[row][col-1]:
                            dp[row][col] = min(1+dp[row-coins[col]][col], dp[row][col-1])
                        else:
                            dp[row][col] = 1+dp[row-coins[col]][col]
            return dp[amount][i]

        ans = solve(coins, amount,len(coins)-1)
        return -1 if math.isinf(ans) else ans