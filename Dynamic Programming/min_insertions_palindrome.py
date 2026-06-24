# question
# =====================
# Minimum number of insertions to make a string palindrome
# Given a string, find the minimum number of characters to be inserted to form Palindrome string out of given string

# Examples:
# ab: Number of insertions required is 1. bab
# aa: Number of insertions required is 0. aa





# # recursion
# # =================================
# def func(a):
#     def longestPallindromeLength(a,b,i,j):
#         if i == 0 or j == 0:
#             return 0
#         if a[i-1] == b[j-1]:
#             return 1+longestPallindromeLength(a,b,i-1,j-1)
#         return max(longestPallindromeLength(a,b,i,j-1), longestPallindromeLength(a,b,i-1,j))
#     return len(a) - longestPallindromeLength(a, a[::-1], len(a), len(a))
    





# # memoization
# # =================================
# def func(a):
#     dp = [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]
#     def longestPallindromeLength(a,b,i,j):
#         if i == 0 or j == 0:
#             return 0
#         if dp[i][j]:
#             return dp[i][j]
#         if a[i-1] == b[j-1]:
#             dp[i][j] = 1+longestPallindromeLength(a,b,i-1,j-1)
#             return dp[i][j]
#         dp[i][j] = max(longestPallindromeLength(a,b,i,j-1), longestPallindromeLength(a,b,i-1,j))
#         return dp[i][j]
#     return len(a) - longestPallindromeLength(a, a[::-1], len(a), len(a))
    



# dp
# =================================
def func(a):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]
    def longestPallindromeLength(a,b,i,j):
        for row in range(1, i+1):
            for col in range(1, j+1):
                if a[row-1] == b[col-1]:
                    dp[row][col] = 1+dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row][col-1], dp[row-1][col])
        return dp[i][j]
        
    return len(a) - longestPallindromeLength(a, a[::-1], len(a), len(a))


# (string, expected_min_insertions)
# Formula: min insertions = len(s) - LPS(s)
test_cases = [
    ("ab",       1),   # problem example; "bab"
    ("aa",       0),   # problem example; already palindrome
    ("abcd",     3),   # LPS=1 → ins=3
    ("",         0),   # empty string
    ("a",        0),   # single char
    ("abcba",    0),   # already palindrome
    ("racecar",  0),   # already palindrome
    ("abca",     1),   # LPS=3("aca") → ins=1
    ("aebcbda",  2),   # LPS=5("abcba") → ins=2
    ("geeks",    3),   # LPS=2("ee") → ins=3
    ("abcde",    4),   # LPS=1 → ins=4
    ("aaaa",     0),   # all same → already palindrome
    ("abcba",    0),   # palindrome
    ("BBABCBCAB",2),   # LPS=7 → ins=2
    ("character",4),   # LPS=5("carac") → ins=4
]

passed = 0
for i, (s, expected) in enumerate(test_cases, 1):
    result = func(s)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {i:2}: {status}  s={s!r} -> {result}  (expected {expected})")

print(f"\n{passed}/{len(test_cases)} tests passed")
