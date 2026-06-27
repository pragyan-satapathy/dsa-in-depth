# https://leetcode.com/problems/find-if-path-exists-in-graph/
# https://leetcode.com/problems/find-if-path-exists-in-graph/submissions/2047975686/ (submission url)


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
        visited = {}  
        def dfs(node):
            if node == destination:
                return True
            visited[node] = node
            for i in map.get(node,[]):
                if i not in visited:
                    if dfs(i):
                        return True 
            return False
        return dfs(source)
        