# question
# =====================
# Dijkstra's Algorithm - Shortest Path in Weighted Graph
# Given a weighted directed graph and a source node, find the shortest distance
# from src to all other nodes. Edge weights must be non-negative.
#
# Approach:
#   1. Initialize distance array with INF; set distance[src] = 0.
#   2. Use a min-heap (priority queue) — push (0, src).
#   3. Pop node with smallest tentative distance (curr_dist, curr_node).
#   4. Skip if curr_dist > distance[curr_node] — entry is stale (shorter path already found).
#   5. For each neighbor, relax edge: if curr_dist + weight < distance[neighbor],
#      update distance and push (new_dist, neighbor) to heap.
#   6. Repeat until heap is empty.
#
# Note: Does NOT handle negative weights.
#   Dijkstra assumes once a node is popped from the heap with distance d,
#   that's the shortest path. But a negative edge discovered later could give
#   a shorter path — breaking that assumption. Use Bellman-Ford for negative weights.

import heapq

def func(src):
    distance = [float('inf')] * len(adj)
    distance[src] = 0
    pq = [(0, src)]                       # (distance, node)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist > distance[curr_node]:
            continue                      # stale entry, already found shorter path
        for neighbor, weight in adj[curr_node]:
            new_dist = curr_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    return distance


# test
# ============
# adj[u] = [(v, weight), ...] — weighted directed graph
# INF = float('inf') means node is unreachable from src

INF = float('inf')

test_cases = [
    # (adj, src, expected_distances)
    (
        [[(1,5),(2,10)], [(2,3)], []],
        0,
        [0, 5, 8],       # 0→1=5, 0→1→2=5+3=8 (cheaper than 0→2=10)
        "3 nodes: indirect path cheaper"
    ),
    (
        [[(1,10),(2,3)], [(2,1),(3,2)], [(1,4),(3,8),(4,2)], [(4,7)], [(3,9)]],
        0,
        [0, 7, 3, 9, 5], # classic dijkstra example
        "5 nodes: classic example"
    ),
    (
        [[(1,5)], [], [(3,2)], []],
        0,
        [0, 5, INF, INF], # nodes 2 and 3 unreachable from 0
        "disconnected: unreachable nodes stay INF"
    ),
    (
        [[]],
        0,
        [0],             # single node, no edges
        "single node"
    ),
    (
        [[(1,1),(2,10)], [(2,1)], []],
        0,
        [0, 1, 2],       # 0→1→2=2 cheaper than direct 0→2=10
        "longer path is cheaper"
    ),
    (
        [[(1,2),(2,6)], [(3,5)], [(3,8)], []],
        0,
        [0, 2, 6, 7],    # 0→1=2, 0→2=6, 0→1→3=7 (cheaper than 0→2→3=14)
        "two paths to dest, pick shorter"
    ),
]

passed = 0
for idx, (graph, src, expected, desc) in enumerate(test_cases, 1):
    adj = graph
    result = func(src)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  {desc}")
    print(f"         result:   {result}")
    print(f"         expected: {expected}")

print(f"\n{passed}/{len(test_cases)} tests passed")