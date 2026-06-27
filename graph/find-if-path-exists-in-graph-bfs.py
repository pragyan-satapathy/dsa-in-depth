# https://leetcode.com/problems/find-if-path-exists-in-graph/
# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/2047795286/ (submission url)

from queue import Queue
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def graph(edges):
            map = {}
            for i in edges:
                if i[0] not in map:
                    map[i[0]] = []
                if i[1] not in map:
                    map[i[1]] = []
                map[i[1]].append(i[0])
                map[i[0]].append(i[1])
            return map
        if source == destination:
            return True
        map = graph(edges)  
        q = Queue()
        q.put(source)
        visited = {source: source}    
        while q.qsize():
            curr = q.get()
            for i in map.get(curr, []):
                if i not in visited:
                    if i == destination:
                        return True
                    visited[i] = i
                    q.put(i)

        return False
        