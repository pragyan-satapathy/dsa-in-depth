# leet code submissions
# ======================
# https://leetcode.com/problems/is-subsequence/submissions/2040866100/

# question
# =====================
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false




# # recursion
# # =================================
# def func(a,b):
#     def helper(a,b,i,j):
#         if i == 0:
#             return True
#         if j == 0:
#             return False
#         if a[i-1] == b[j-1]:
#             return helper(a,b,i-1,j-1)
#         return helper(a,b,i,j-1)
#     return helper(a, b, len(a), len(b))
    





# # memoization
# # =================================
# def func(a,b):
#     dp = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
#     def helper(a,b,i,j):
#         if i == 0:
#             return True
#         if j == 0:
#             return False
#         if (dp[i][j]):
#             return dp[i][j]
#         if a[i-1] == b[j-1]:
#             dp[i][j] = helper(a,b,i-1,j-1)
#             return dp[i][j]
#         dp[i][j] = helper(a,b,i,j-1)
#         return dp[i][j]
#     return helper(a, b, len(a), len(b))



# dp
# =================================
def func(a,b):
    dp = [[False for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    def helper(a,b,i,j):
        for row in range(len(a)+1):
            for col in range(len(b)+1):
                if row == 0:
                    dp[row][col] = True
                elif col == 0:
                    dp[row][col] = False
                elif a[row-1] == b[col-1]:
                    dp[row][col] = dp[row-1][col-1]
                else:
                   dp[row][col] = dp[row][col-1]
        return dp[i][j]
    return helper(a, b, len(a), len(b))


# (s, t, expected)
test_cases = [
    ("abc",  "ahbgdc",   True),    # example 1
    ("axc",  "ahbgdc",   False),   # example 2
    ("",     "ahbgdc",   True),    # empty s is always a subsequence
    ("",     "",         True),    # both empty
    ("a",    "",         False),   # non-empty s, empty t
    ("a",    "a",        True),    # single char match
    ("a",    "b",        False),   # single char no match
    ("ace",  "abcde",    True),    # classic example
    ("aec",  "abcde",    False),   # order matters
    ("abc",  "abc",      True),    # s equals t
    ("abcd", "abc",      False),   # s longer than t
    ("bb",   "ahbgdc",   False),   # only one 'b' in t
    ("bb",   "ahbbgdc",  True),    # two 'b's in t
    ("xyz",  "xaybzc",   True),    # spread across t
    ("xyz",  "zyx",      False),   # reversed order
]

passed = 0
for i, (s, t, expected) in enumerate(test_cases, 1):
    result = func(s, t)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {i:2}: {status}  s={s!r} t={t!r} -> {result}  (expected {expected})")

print(f"\n{passed}/{len(test_cases)} tests passed")
