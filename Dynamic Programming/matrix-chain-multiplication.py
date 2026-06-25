# question
# =====================
# Matrix Chain Multiplication using Recursion
#  Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to  perform the multiplications, but merely to decide in which order to perform the multiplications. 





# # recursion
# # =================================
# def mcm(a,i,j):
#     if i>=j:
#         return 0
#     res = float('inf')
#     for k in range(i,j):
#         temp = mcm(a,i,k)+mcm(a,k+1,j)+(a[i-1]*a[k]*a[j])
#         res = min(res,temp)
#     return res
    





# memoization
# =================================
def mcm(a,i,j):
    dp = [[0 for _ in range(len(a)+1)] for _ in range(len(a)+1)]
    def func(a,i,j):
        if i>=j:
            return 0
        if dp[i][j]:
            return dp[i][j]
        res = float('inf')
        for k in range(i,j):
            temp = func(a,i,k)+func(a,k+1,j)+(a[i-1]*a[k]*a[j])
            res = min(res,temp)
        dp[i][j] = res
        return res
    return func(a,1,len(a)-1)
    


    


# (dims, expected_min_ops)
# dims is array of matrix dimensions: dims[i-1] x dims[i] for matrix i
# call: mcm(dims, 1, len(dims)-1)
test_cases = [
    ([10, 20, 30],              6000),   # 2 matrices: only one split → 10*20*30=6000
    ([10, 30, 5, 60],           4500),   # 3 matrices; optimal order gives 4500 (classic example) → actually (10x30x5) + (10x5x60) = 1500+3000=4500? let me recheck: split at k=1: 10*30*60+30*5*60=18000+9000=27000; k=2: 10*30*5+10*5*60=1500+3000=4500; k=3 invalid. so 4500
    ([40, 20, 30, 10, 30],      26000),  # 4 matrices
    ([10, 20, 30, 40, 30],      30000),  # 4 matrices
    ([1, 2, 3, 4],              18),     # small dims
    ([2, 3, 4],                 24),     # 2 matrices: only one split → 2*3*4=24
    ([5, 10, 3, 12, 5, 50, 6], 2010),   # 6 matrices
    ([10, 10, 10],              1000),   # 2 identical square matrices
    ([1, 1, 1, 1],              2),      # all 1s → min ops = 2
    ([3, 2, 5, 2],              32),     # 3 matrices; min split gives 32
]

passed = 0
for idx, (dims, expected) in enumerate(test_cases, 1):
    result = mcm(dims, 1, len(dims)-1)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  dims={dims} -> {result}  (expected {expected})")

print(f"\n{passed}/{len(test_cases)} tests passed")
