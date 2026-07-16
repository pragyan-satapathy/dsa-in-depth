# https://leetcode.com/problems/majority-element/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# https://leetcode.com/problems/majority-element/submissions/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach 1: Hash map count
# Count every element and return whichever appears more than n//2 times.
# Time: O(n)  Space: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = Counter(nums)
        req = len(nums)//2    # threshold: must appear strictly more than half the time
        for i in a:
            print(i, a[i], req)
            if a[i] > req:
                return i


# Approach 2: Boyer-Moore Voting Algorithm
# https://leetcode.com/problems/majority-element/submissions/2068263179/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# Intuition: the majority element appears > n/2 times, so it can never be fully
# "cancelled out" by all other elements combined.
# Maintain a candidate and a net vote count:
#   - When count hits 0, adopt the current element as the new candidate.
#   - Same as candidate → +1 (a vote for it).
#   - Different → -1 (a vote against it, cancelling one occurrence).
# The surviving candidate at the end is guaranteed to be the majority element.
# Time: O(n)  Space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        for i in nums:
            if count == 0:         # no current candidate — adopt this element
                count += 1
                candidate = i
            elif candidate == i:   # reinforce the current candidate
                count += 1
            else:                  # cancel one vote against the candidate
                count -= 1
        return candidate
