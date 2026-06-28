# https://leetcode.com/problems/reconstruct-itinerary/submissions/2048728259/

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        # Build adjacency list from the given tickets.
        for src, dst in tickets:
            if src not in graph:
                graph[src] = []
            graph[src].append(dst)

        # Sort destinations in reverse lexicographical order so that
        # popping from the end always gives the smallest destination.
        for node in graph:
            graph[node].sort(reverse=True)

        path = []

        # Hierholzer's Algorithm:
        # Keep traversing unused edges until a node has no outgoing edges.
        # Only then add the node to the itinerary (postorder traversal).
        def dfs(node):
            while graph.get(node):
                nxt = graph[node].pop()   # Consume the lexicographically smallest unused ticket.
                dfs(nxt)

            # Add the airport after all its outgoing tickets are used.
            path.append(node)

        dfs("JFK")

        # The itinerary is built in reverse, so reverse it before returning.
        return path[::-1]