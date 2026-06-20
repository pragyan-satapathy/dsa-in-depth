# # question
# # =====================
# # Minimum number of deletions and insertions to transform one string into another
# # Given two strings ‘str1’ and ‘str2’ of size m and n respectively. The task is to remove/delete and insert minimum number of characters from/in str1 so as to transform it into str2. It could be possible that the same character needs to be removed/deleted from one point of str1 and inserted to some another point.
# # Example:
# # Input : str1 = "geeksforgeeks", str2 = "geeks"
# # Output : Minimum Deletion = 8
# #          Minimum Insertion = 0 



# # recursion
# # =================================
# def func(a, b):
#     def lcs(a,b,i,j):
#         if i == 0 or j == 0:
#             return 0
#         if a[i-1] == b[j-1]:
#             return 1+lcs(a,b,i-1,j-1)
#         return max(lcs(a,b,i-1,j),lcs(a,b,i,j-1))
#     common = lcs(a, b, len(a), len(b))
#     deleteCount = len(a) - common
#     insertCount = len(b) - common
#     return {deleteCount, insertCount}




# # memoization
# # =================================
# def func(a, b):
#     dp = [[0 for _ in range (len(b)+1)] for _ in range (len(a)+1)]
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

#     common = lcs(a, b, len(a), len(b))
#     deleteCount = len(a) - common
#     insertCount = len(b) - common
#     return {deleteCount, insertCount}



# dp
# =================================
def func(a, b):
    dp = [[0 for _ in range (len(b)+1)] for _ in range (len(a)+1)]
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

    common = lcs(a, b, len(a), len(b))
    deleteCount = len(a) - common
    insertCount = len(b) - common
    return {deleteCount, insertCount}


# (str1, str2, expected_deletions, expected_insertions)
# Formula: deletions = len(str1) - LCS,  insertions = len(str2) - LCS
# func returns a set {deleteCount, insertCount}
test_cases = [
    ("geeksforgeeks", "geeks",    8, 0),   # problem example; LCS=5 → del=8, ins=0
    ("geeks",  "geeksforgeeks",   0, 8),   # reverse of above
    ("heap",   "help",            1, 1),   # LCS="hep"(3) → del=1, ins=1
    ("ABCDEF", "ABCDEF",          0, 0),   # identical strings
    ("ABCDEF", "ACE",             3, 0),   # "ACE" is subseq of "ABCDEF" → del=3, ins=0
    ("ABC",    "DEF",             3, 3),   # no common chars
    ("",       "ABC",             0, 3),   # str1 empty
    ("ABC",    "",                3, 0),   # str2 empty
    ("",       "",                0, 0),   # both empty
    ("A",      "A",               0, 0),   # single identical char
    ("A",      "B",               1, 1),   # single different char
    ("ABCBDAB","BDCAB",           3, 1),   # LCS=4 → del=3, ins=1
    ("AGGTAB", "GXTXAYB",         2, 3),   # LCS=4 → del=2, ins=3
    ("abcde",  "ace",             2, 0),   # "ace" subseq of "abcde" → del=2, ins=0
    ("aaa",    "aa",              1, 0),   # repeated chars, LCS=2 → del=1, ins=0
    ("abcd",   "dcba",            3, 3),   # reversed string, LCS=1
]

passed = 0
for i, (s1, s2, exp_del, exp_ins) in enumerate(test_cases, 1):
    result = func(s1, s2)
    ok = result == {exp_del, exp_ins}
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {i:2}: {status}  str1={s1!r} str2={s2!r} -> {result}  (expected del={exp_del} ins={exp_ins})")

print(f"\n{passed}/{len(test_cases)} tests passed")
