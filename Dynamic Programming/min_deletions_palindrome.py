# question
# =====================
# Minimum number of deletions to make a string palindrome
# Given a string of size ‘n’. The task is to remove or delete minimum number of characters from the string so that the resultant string is palindrome.
# Examples :

# Input : aebcbda
# Output : 2
# Remove characters 'e' and 'd'
# Resultant string will be 'abcba'
# which is a palindromic string



# # recursion
# # =================================
# def func(a):
#     def lcs(a,b,i,j):
#         if i == 0 or j == 0:
#             return 0
#         if a[i-1] == b[j-1]:
#             return 1+lcs(a,b,i-1,j-1)
#         return max(lcs(a,b,i-1,j),lcs(a,b,i,j-1))
#     return len(a)-lcs(a, a[::-1], len(a), len(a))
    




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

#     return len(a)-lcs(a, a[::-1], len(a), len(a))



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
    return len(a)-lcs(a, a[::-1], len(a), len(a))


# (string, expected_min_deletions)
# Formula: min deletions = len(s) - LPS(s)
test_cases = [
    ("aebcbda",   2),   # problem example; remove 'e','d' → "abcba"
    ("abcba",     0),   # already a palindrome
    ("abcd",      3),   # LPS=1 → del=3
    ("",          0),   # empty string
    ("a",         0),   # single char is palindrome
    ("aa",        0),   # already palindrome
    ("ab",        1),   # LPS=1 → del=1
    ("abca",      1),   # LPS=3("aca") → del=1
    ("geeks",     3),   # LPS=2("ee") → del=3
    ("aebcbda",   2),   # LPS=5("abcba") → del=2
    ("BBABCBCAB", 2),   # LPS=7("BABCBAB") → del=2
    ("racecar",   0),   # already palindrome
    ("abcde",     4),   # LPS=1 → del=4
    ("aabaa",     0),   # already palindrome
    ("character", 4),   # LPS=5("carac") → del=4
]

passed = 0
for i, (s, expected) in enumerate(test_cases, 1):
    result = func(s)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {i:2}: {status}  s={s!r} -> {result}  (expected {expected})")

print(f"\n{passed}/{len(test_cases)} tests passed")
