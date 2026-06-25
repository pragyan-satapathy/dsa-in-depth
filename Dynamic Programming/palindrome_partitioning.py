# question
# =====================
# Palindrome Partitioning using Recursion
# Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. 
# Example:
#   “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”.








# # recursion
# # =================================
# def func(a,i,j):
#     if i>j:
#         return 0
#     if isPallindrom(a[i:j+1]):
#         return 0
#     res = float('inf')
#     for k in range(i,j):
#         temp = func(a,i,k)+1+func(a,k+1,j)
#         res = min(res,temp)
#     return res
def isPallindrom(a):
    if a == a[::-1]:
        return True
    return False
    





#  # memoization
#  # =================================
# def func(a,i,j):
#     dp = [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]
#     def fun(a,i,j):
#         if i>j:
#             return 0
#         if dp[i][j]:
#             return dp[i][j]
#         if isPallindrom(a[i:j+1]):
#             return 0
#         res = float('inf')
#         for k in range(i,j):
#             temp = fun(a,i,k)+1+fun(a,k+1,j)
#             res = min(res,temp)
#         dp[i][j] = res
#         return dp[i][j]
#     return fun(a,i,j)
    



# optimized meoization
# ======================================
def func(a,i,j):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]
    def fun(a,i,j):
        if i>j:
            return 0
        if dp[i][j]:
            return dp[i][j]
        if isPallindrom(a[i:j+1]):
            return 0
        res = float('inf')
        for k in range(i,j):
            if (not dp[i][k]):
                left = fun(a,i,k)
            else:
                left = dp[i][k]
            if (not dp[k+1][j]):
                right = fun(a,k+1,j)
            else:
                right = dp[k+1][j]
            
            temp = left+1+right
            res = min(res,temp)
        dp[i][j] = res
        return dp[i][j]
    return fun(a,i,j)


    


# (string, min_cuts)
# call: func(s, 0, len(s)-1)
test_cases = [
    ("a",                    0),   # single char → palindrome
    ("aa",                   0),   # palindrome
    ("ab",                   1),   # "a|b"
    ("aab",                  1),   # "aa|b"
    ("abc",                  2),   # "a|b|c"
    ("abba",                 0),   # palindrome
    ("abcba",                0),   # palindrome
    ("abcd",                 3),   # "a|b|c|d"
    ("aaaa",                 0),   # all same → palindrome
    ("aabb",                 1),   # "aa|bb"
    ("abcbm",                2),   # "a|bcb|m"
    ("ababab",               1),   # "aba|bab"
    ("aabaa",                0),   # palindrome
    ("racecar",              0),   # palindrome
    ("abacaba",              0),   # palindrome
    ("ababbbabbababa",       3),   # "aba|bb|babbab|aba"
]

passed = 0
for idx, (s, expected) in enumerate(test_cases, 1):
    result = func(s, 0, len(s)-1)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  s={s!r:25} -> {result}  (expected {expected})")

print(f"\n{passed}/{len(test_cases)} tests passed")
