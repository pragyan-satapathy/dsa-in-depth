# https://leetcode.com/problems/sort-characters-by-frequency/submissions/2062548039/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Bucket by frequency
# 1. Count occurrences of each character.
# 2. Group characters by their frequency into a dict: freq → [chars].
# 3. Iterate frequencies in descending order, appending each char repeated f times.
# Time: O(n + k log k)  where k = number of distinct characters  Space: O(k)

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: count each character's frequency
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Step 2: invert — map frequency → list of characters with that frequency
        freq = {}
        for ch, f in count.items():
            freq.setdefault(f, []).append(ch)

        # Step 3: build result by appending chars from highest to lowest frequency
        res = ""
        for f in sorted(freq.keys(), reverse=True):
            for ch in freq[f]:
                res += (ch * f)   # repeat the character f times
        return res


# Optimal Approach: Bucket Sort
# https://leetcode.com/problems/sort-characters-by-frequency/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days
# A character can appear at most len(s) times, so we can use an array of size
# len(s)+1 as buckets indexed by frequency — eliminating the sort step entirely.
# Time: O(n)  Space: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        # bucket[f] holds all characters that appear exactly f times
        bucket = [[] for _ in range(len(s) + 1)]
        count = Counter(s)
        for ch, freq in count.items():
            bucket[freq].append(ch)

        res = []
        # iterate from highest frequency down to 1, collecting characters
        for freq in range(len(s), 0, -1):
            for ch in bucket[freq]:
                res.append(ch * freq)   # repeat the character freq times

        return "".join(res)