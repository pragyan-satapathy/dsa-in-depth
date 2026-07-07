# question
# =====================
# Bellman-Ford Algorithm - Single-Source Shortest Path with Negative Weights
# Given a weighted directed graph with V nodes, a list of edges (u, v, w),
# and a source node, find the shortest distance from src to all other nodes.
# Can handle negative edge weights and detect negative cycles.
#
# Approach:
#   1. Initialize distance array with INF; set dist[src] = 0.
#   2. Repeat V-1 times (a shortest simple path has at most V-1 edges):
#        For every edge (u, v, w), relax: if dist[u] + w < dist[v], update dist[v].
#        If no relaxation occurs in a full pass, shortest paths are found — exit early.
#   3. Do one more pass over all edges:
#        If any edge still relaxes, a negative cycle exists — return a warning.
#   4. Return the distance array.
#
# Note: Unlike Dijkstra, works with negative weights because it doesn't greedily
#   finalize nodes. It relaxes ALL edges V-1 times, guaranteeing shortest paths
#   since any simple path visits at most V-1 edges.

def func(V, edges, src):
    dist = [float('inf')] * V
    dist[src] = 0
    for i in range(V - 1):
        flag = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                flag = True
        if not flag:
            return dist               # no more relaxation requied — done early
    for u, v, w in edges:
        if dist[v] != float('inf') and dist[u] + w < dist[v]:
            return "Negative weight Cycle detected"
    return dist


# test
# ============
# edges: list of (u, v, w) — weighted directed edge from u to v with weight w
# INF = float('inf') means node is unreachable from src

INF = float('inf')

test_cases = [
    (
        3,
        [(0,1,4),(1,2,3)],
        0,
        [0, 4, 7],
        "simple path: 0→1→2"
    ),
    (
        4,
        [(0,1,5),(0,2,7),(1,2,-2),(1,3,6),(2,3,1)],
        0,
        [0, 5, 3, 4],
        "negative edge: 0→1→2 = 5-2=3, cheaper than direct 0→2=7"
    ),
    (
        4,
        [(0,1,2),(0,2,6),(1,2,1),(1,3,5),(2,3,8)],
        0,
        [0, 2, 3, 7],
        "two paths to each node, pick shorter"
    ),
    (
        3,
        [(1,2,3),(0,1,4)],
        0,
        [0, 4, 7],
        "edge order shouldn't matter — needs multiple passes"
    ),
    (
        3,
        [(0,1,5)],
        0,
        [0, 5, INF],
        "disconnected node stays INF"
    ),
    (
        3,
        [(0,1,1),(1,2,1),(2,0,-3)],
        0,
        "Negative weight Cycle detected",
        "negative cycle: 0→1→2→0 has total weight -1"
    ),
]

passed = 0
for idx, (V, edges, src, expected, desc) in enumerate(test_cases, 1):
    result = func(V, edges, src)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  {desc}")
    if not ok:
        print(f"         result:   {result}")
        print(f"         expected: {expected}")

print(f"\n{passed}/{len(test_cases)} tests passed")
