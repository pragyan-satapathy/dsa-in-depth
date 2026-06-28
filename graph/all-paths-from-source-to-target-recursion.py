# https://leetcode.com/problems/all-paths-from-source-to-target/submissions/2048106394/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)-1
        def dfs(node, path=[]):
            for i in graph[node[-1]]:
                if i == n:
                    ans.append(node+[i])
                else:
                    path.append(node+[i])
            if len(path):
                curr = path.pop()
                return dfs(curr, path)
            else:
                print(ans)
                return ans
        return dfs([0])