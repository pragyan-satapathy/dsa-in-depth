# question
# =====================
# Shortest Path (with path reconstruction) in Unweighted Graph (BFS)
# Given an unweighted graph, find the shortest path (list of nodes) from src to dest.
#
# Approach:
#   1. Enqueue [src, [src]] — node paired with its path from src.
#   2. Pop curr; if curr node == dest, return the path immediately.
#   3. For each unvisited neighbor, enqueue [nei, path + [nei]].
#   4. BFS guarantees the first time dest is reached is via the shortest path.
#   5. Return None if dest is unreachable.

from queue import Queue
visited = set()
def bfs_distances(src, destination):
	q = Queue()
	q.put([src, [src]])        # [node, path_so_far]
	visited.add(src)
	while(q.qsize()):
		curr = q.get()
		if (curr[0] == destination):
			return curr[1]     # return path when dest is reached
		for nei in adj[curr[0]]:
			if nei not in visited:
				visited.add(nei)
				q.put([nei, curr[1] + [nei]])   # extend path
	return None                # if no path found


# test
# ============
# expected output format: list of nodes from src to dest (shortest path)

test_cases = [
    (
        [[1, 2], [0, 3], [0, 3], [1, 2, 4], [3]],
        0, 4,
        [[0, 1, 3, 4], [0, 2, 3, 4]],   # two valid shortest paths
        "src=0 dest=4"
    ),
    (
        [[1], [0, 2], [1, 3], [2]],
        0, 3,
        [[0, 1, 2, 3]],
        "chain: src=0 dest=3"
    ),
    (
        [[1, 2], [0, 2], [0, 1]],
        0, 2,
        [[0, 2]],                        # direct edge
        "triangle: src=0 dest=2"
    ),
    (
        [[1], [0], [3], [2]],
        0, 3,
        [None],                          # disconnected graph
        "no path exists"
    ),
    (
        [[1, 2], [0, 3], [0, 3], [1, 2]],
        0, 0,
        [[0]],                           # src == dest
        "src == dest"
    ),
]

passed = 0
for idx, (graph, src, dest, valid_paths, desc) in enumerate(test_cases, 1):
    adj = graph
    visited = set()
    result = bfs_distances(src, dest)
    ok = result in valid_paths
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  {desc}")
    print(f"         result:   {result}")
    print(f"         expected: {valid_paths}")

print(f"\n{passed}/{len(test_cases)} tests passed")
