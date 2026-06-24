# question
# =====================
# Matrix Chain Multiplication using Recursion
#  Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to  perform the multiplications, but merely to decide in which order to perform the multiplications. 





# recursion
# =================================
def mcm(a,i,j):
    if i>=j:
        return 0
    res = float('inf')
    for k in range(i,j):
        temp = mcm(a,i,k)+mcm(a,k+1,j)+(a[i-1]*a[k]*a[j])
        res = min(res,temp)
    return res
    