# https://leetcode.com/problems/k-th-symbol-in-grammar/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/k-th-symbol-in-grammar/submissions/2066908322/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        ans = self.kthGrammar(n-1, (k+1) // 2)
        if k%2:
            return ans
        else:
            if ans:
                return 0
            else: 
                return 1