# https://leetcode.com/problems/rotting-oranges/submissions/2062789967/?envType=company&envId=microsoft&favoriteSlug=microsoft-thirty-days

# Approach: Multi-source BFS
# All initially rotten oranges are sources — seed them into the queue simultaneously.
# BFS spreads rotting level by level (minute by minute).
# Each node carries its timestamp (a[2]) so we know how many minutes it took.
# At the end, if any cell was never visited, some fresh orange is unreachable → -1.
# Time: O(m*n)  Space: O(m*n)

from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = Queue()
        visited = set()
        fresh = 0
        rotten = 0

        # seed queue with all initially rotten oranges (minute 0)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.put((i, j, 0))   # (row, col, minute)
                    visited.add((i, j))
                    rotten += 1
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:   # no fresh oranges to rot
            return 0

        count = 0   # total cells processed (fresh + rotten)
        level = 0   # latest minute recorded

        while q.qsize():
            a = q.get()
            count += 1

            # check all 4 neighbours; enqueue if fresh and not yet visited
            if (
                a[0] - 1 >= 0 and
                (a[0]-1, a[1]) not in visited and
                grid[a[0]-1][a[1]] == 1     # up
            ):
                visited.add((a[0]-1, a[1]))
                q.put((a[0]-1, a[1], a[2]+1))
                level = max(level, a[2]+1)

            if (
                a[1] - 1 >= 0 and
                (a[0], a[1]-1) not in visited and
                grid[a[0]][a[1]-1]          # left
            ):
                visited.add((a[0], a[1]-1))
                q.put((a[0], a[1]-1, a[2]+1))
                level = max(level, a[2]+1)

            if (
                a[0] + 1 < len(grid) and
                (a[0]+1, a[1]) not in visited and
                grid[a[0]+1][a[1]]          # down
            ):
                visited.add((a[0]+1, a[1]))
                q.put((a[0]+1, a[1], a[2]+1))
                level = max(level, a[2]+1)

            if (
                a[1] + 1 < len(grid[0]) and
                (a[0], a[1]+1) not in visited and
                grid[a[0]][a[1]+1]          # right
            ):
                visited.add((a[0], a[1]+1))
                q.put((a[0], a[1]+1, a[2]+1))
                level = max(level, a[2]+1)

        # if we didn't visit every orange, some fresh orange was isolated
        if count < fresh + rotten:
            return -1
        return level
        