# https://leetcode.com/problems/all-paths-from-source-to-target/submissions/2048061637/

from queue import Queue
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        path = Queue()
        ans = []
        for i in graph[0]:
            if i == len(graph)-1:
                ans.append([0,i])
            else:
                path.put([0,i])
        while(path.qsize()):
            curr = path.get()
            print(curr)
            for i in graph[curr[-1]]:
                if i == len(graph)-1:
                    ans.append(curr+[i])
                else:
                    path.put(curr+[i])
        return ans