# https://leetcode.com/contest/weekly-contest-507/problems/maximum-manhattan-distance-after-all-moves/

class Solution:
    def maxDistance(self, moves: str) -> int:
        d = {}
        for i in moves:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return (
            abs(d.get('U', 0) - d.get('D', 0))
            + abs(d.get('L', 0) - d.get('R', 0))
            + d.get('_', 0)
        )