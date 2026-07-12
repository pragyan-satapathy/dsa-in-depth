# https://leetcode.com/problems/combination-sum/description/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/combination-sum/submissions/2063475417/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Backtracking (include/exclude)
# At each index i we make two choices:
#   1. Exclude candidates[i] — move to i-1 with the same remaining target.
#   2. Include candidates[i] — stay at i (can reuse the same element) and reduce target.
# We iterate from the last index down to 0, which naturally avoids duplicate combinations
# (each candidate is only considered at its own index and to the left).
# Time: O(2^t) in the worst case where t = target  Space: O(t) recursion depth

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def func(i, t, pattern):
            if t == 0:         # found a valid combination
                res.append(pattern)
                return
            if i < 0:          # exhausted all candidates
                return
            if candidates[i] > t:
                # current candidate is too large — skip it and try smaller ones
                func(i-1, t, pattern)
                return
            # choice 1: exclude candidates[i]
            func(i-1, t, pattern)
            # choice 2: include candidates[i] (stay at i to allow reuse)
            func(i, t - candidates[i], pattern + [candidates[i]])

        func(len(candidates) - 1, target, [])
        return res
        