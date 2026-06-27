# BFS (https://leetcode.com/problems/clone-graph/submissions/2047748431/)
# ========
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from queue import Queue
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:                        # if input is NULL, return NULL
            return None
        q = Queue()
        q.put(node)
        root = Node(node.val)
        visited = {node: root}                    # map: original node → cloned node
        while(q.qsize()):
            curr = q.get()
            for i in curr.neighbors:
                if i not in visited:              # not visited yet
                    q.put(i)
                    visited[i] = Node(i.val)      # create clone and add to map
                visited[curr].neighbors.append(visited[i])  # link cloned neighbor
        return root                         # return cloned root
        







# DFS (https://leetcode.com/problems/clone-graph/submissions/2047751211/)
# ========
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        stack = [node]
        root = Node(node.val)
        visited = {node: root}
        while(len(stack)):
            curr = stack.pop()
            for i in curr.neighbors:
                if i not in visited:
                    visited[i] = Node(i.val)
                    stack.append(i)
                visited[curr].neighbors.append(visited[i])
        return root
        