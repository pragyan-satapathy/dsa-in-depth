# question
# =====================
# Shortest Path in Unweighted Graph (BFS)
# Given an unweighted undirected graph and a source node, find the shortest distance
# (minimum number of edges) from the source to every other reachable node.
#
# Approach:
#   1. Start BFS from the source node with distance 0.
#   2. For each node popped from the queue, record {vertic, dist} in result.
#   3. For each unvisited neighbor, mark visited and enqueue with dist+1.
#   4. BFS guarantees shortest distance since it explores level by level.

from queue import Queue
path = []
visited = set()
def bfs_distances(node):
	q = Queue()
	q.put([node, 0])
	visited.add(node)
	while(q.qsize()):
		curr = q.get()
		path.append({"vertic": curr[0], "dist": curr[1]})
		for nei in adj[curr[0]]:
			if nei not in visited:
				visited.add(nei)
				q.put([nei, curr[1]+1])
	return path


# test
# ============
# expected output format: [{vertic: node, dist: distance}, ...]

test_cases = [
    (
        [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3]],
        0,
        [{'vertic': 0, 'dist': 0}, {'vertic': 1, 'dist': 1}, {'vertic': 2, 'dist': 1}, {'vertic': 3, 'dist': 2}, {'vertic': 4, 'dist': 3}],
        "simple graph from node 0"
    ),
    (
        [[1], [0, 2], [1, 3], [2]],
        0,
        [{'vertic': 0, 'dist': 0}, {'vertic': 1, 'dist': 1}, {'vertic': 2, 'dist': 2}, {'vertic': 3, 'dist': 3}],
        "chain: 0-1-2-3"
    ),
    (
        [[1, 2], [0, 2], [0, 1]],
        0,
        [{'vertic': 0, 'dist': 0}, {'vertic': 1, 'dist': 1}, {'vertic': 2, 'dist': 1}],
        "triangle from node 0"
    ),
]

passed = 0
for idx, (graph, src, expected, desc) in enumerate(test_cases, 1):
    adj = graph
    path = []
    visited = set()
    result = bfs_distances(src)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  {desc}")
    print(f"         result:   {result}")
    print(f"         expected: {expected}")

print(f"\n{passed}/{len(test_cases)} tests passed")
