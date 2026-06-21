# question
# =====================
# Longest Palindromic Subsequence
# Given a sequence, find the length of the longest palindromic subsequence in it.
# Example :
# Input:"bbbab"
# Output:4



# # recursion
# # =================================
# def func(a):
#     def lcs(a,b,i,j):
#         if i == 0 or j == 0:
#             return 0
#         if a[i-1] == b[j-1]:
#             return 1+lcs(a,b,i-1,j-1)
#         return max(lcs(a,b,i-1,j),lcs(a,b,i,j-1))
#     return lcs(a, a[::-1], len(a), len(a))
    




# # memoization
# # =================================
# def func(a):
#     dp =  [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]
#     def lcs(a,b,i,j):
#         if i == 0 or j == 0:
#             return 0
#         if dp[i][j]:
#             return dp[i][j]
#         if a[i-1] == b[j-1]:
#             dp[i][j] = 1+lcs(a,b,i-1,j-1)
#             return dp[i][j] 
#         dp[i][j] = max(lcs(a,b,i-1,j),lcs(a,b,i,j-1))
#         return dp[i][j] 

#     return lcs(a, a[::-1], len(a), len(a))



# dp
# =================================
def func(a):
    dp = [[0 for _ in range (len(a)+1)] for _ in range (len(a)+1)]
    def lcs(a,b,i,j):
        for row in range(1,i+1):
            for col in range(1, j+1):
                if dp[row][col]:
                    return dp[row][col]
                if a[row-1] == b[col-1]:
                    dp[row][col] = 1+dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col],dp[row][col-1])
        return dp[i][j]

    return lcs(a, a[::-1], len(a), len(a))


# (string, expected_lps_length)
# Approach: LPS(s) = LCS(s, reverse(s))
test_cases = [
    ("bbbab",     4),   # problem example; "bbbb"
    ("cbbd",      2),   # "bb"
    ("abcba",     5),   # whole string is a palindrome
    ("abcd",      1),   # all unique → any single char
    ("",          0),   # empty string
    ("a",         1),   # single char
    ("aa",        2),   # two same chars
    ("aba",       3),   # whole string is a palindrome
    ("racecar",   7),   # whole string is a palindrome
    ("aabaa",     5),   # whole string is a palindrome
    ("agbdba",    5),   # "abdba"
    ("BBABCBCAB", 7),   # "BABCBAB"
    ("character", 5),   # "carac"
    ("aaaa",      4),   # all same chars
    ("abacaba",   7),   # whole string is a palindrome
]

passed = 0
for i, (s, expected) in enumerate(test_cases, 1):
    result = func(s)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {i:2}: {status}  s={s!r} -> {result}  (expected {expected})")

print(f"\n{passed}/{len(test_cases)} tests passed")
