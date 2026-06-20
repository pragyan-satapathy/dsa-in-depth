# Question
# ==============================
# Shortest Common SuperSequence
# Given two strings str1 and str2, find the shortest string that has both str1 and str2 as subsequences.
# Examples:

# Input:   str1 = "geek",  str2 = "eke"
# Output: "geeke"

def helper(a, b):
    dp = [["" for _ in range (len(b)+1)] for _ in range (len(a)+1)]
    def func(a,b,i,j):
        for row in range (len(a)+1):
            for col in range(len(b)+1):
                if row == 0:
                    dp[row][col] = b[0:col]
                elif col == 0:
                    dp[row][col] = a[0:row]
                elif  a[row-1] == b[col-1]:
                    dp[row][col] = dp[row-1][col-1]+a[row-1]
                else:
                    r1 = dp[row-1][col]+a[row-1]
                    r2 = dp[row][col-1]+b[col-1]
                    if (len(r1) < len(r2)):
                        dp[row][col] = r1
                    else:
                        dp[row][col] =  r2

        return dp[i][j]

        # # memoization
        # if i == 0:
        #     return b[0:j]
        # if j == 0:
        #     return a[0:i]
        # if (dp[i][j]):
        #     return dp[i][j]
        # if  (a[i-1] == b[j-1]):
        #     dp[i][j] = func(a,b,i-1,j-1)+a[i-1]
        #     return dp[i][j]
        # r1 = func(a,b,i-1,j)+a[i-1]
        # r2 = func(a,b,i,j-1)+b[j-1]
        # if (len(r1) < len(r2)):
        #     dp[i][j] = r1
        # else:
        #     dp[i][j] =  r2
        # return dp[i][j]
    return func(a, b, len(a), len(b))


# (a, b, expected_scs_length) — SCS length = len(a) + len(b) - LCS(a, b)
# we check length since multiple valid SCS strings may exist
test_cases = [
    ("geek",    "eke",      5),   # "geeke"
    ("ABCBDAB", "BDCAB",    8),   # LCS=4 → 7+5-4=8
    ("AGGTAB",  "GXTXAYB",  9),   # LCS=4 → 6+7-4=9
    ("ABCDEF",  "ABCDEF",   6),   # identical → SCS = either string
    ("ABC",     "AC",       3),   # "AC" is subseq of "ABC" → SCS = "ABC"
    ("ABC",     "DEF",      6),   # no common chars → full concat
    ("",        "ABC",      3),   # one empty → SCS = other string
    ("ABC",     "",         3),   # one empty → SCS = other string
    ("A",       "A",        1),   # identical single char
    ("A",       "B",        2),   # no common → "AB" or "BA"
    ("ABCD",    "XYCD",     6),   # LCS="CD"(2) → 4+4-2=6
    ("abcde",   "ace",      5),   # "ace" is subseq of "abcde" → SCS = "abcde"
    ("STONE",   "LONGEST",  9),   # LCS=3 → 5+7-3=9
]

passed = 0
for i, (a, b, expected_len) in enumerate(test_cases, 1):
    result = helper(a, b)
    got_len = len(result)
    status = "PASS" if got_len == expected_len else "FAIL"
    if got_len == expected_len:
        passed += 1
    print(f"Test {i}: {status}  a={a!r} b={b!r} -> scs={result!r} (len={got_len}), expected len={expected_len}")

print(f"\n{passed}/{len(test_cases)} tests passed")
