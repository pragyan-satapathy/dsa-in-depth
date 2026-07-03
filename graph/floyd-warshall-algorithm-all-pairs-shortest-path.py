# question
# =====================
# Floyd-Warshall Algorithm - All-Pairs Shortest Path
# Given a weighted directed graph with V nodes and a list of edges (u, v, w),
# find the shortest distance between every pair of nodes.
# Edge weights may be negative, but negative cycles are not allowed.
#
# Approach:
#   1. Initialize a V×V distance matrix: 0 on diagonal, INF elsewhere.
#   2. Fill in direct edge weights: mat[u][v] = w.
#   3. For each intermediate node k (0 to V-1):
#        For every pair (row, col), relax: mat[row][col] = min(mat[row][col], mat[row][k] + mat[k][col])
#        This asks: "is going through k shorter than the current known path?"
#   4. After all k iterations, mat[i][j] holds the shortest distance from i to j.
#
# Note: Unlike Dijkstra (single-source), Floyd-Warshall computes shortest paths
#   for ALL pairs in O(V³) time and O(V²) space. Handles negative weights
#   but not negative cycles.

def floyd_warshall(V, edges):
    mat = [[0 if i == j else float('inf') for j in range(V)] for i in range(V)]
    for u,v,w  in edges:
        mat[u][v] = w
    for k in range(V):
        for row in range(len(mat)):
            for col in range(len(mat)):
                mat[row][col] = min(mat[row][col], mat[row][k]+mat[k][col])
    return mat
    
# test
# ============
# floyd_warshall(V, edges) → V×V matrix where mat[i][j] = shortest distance from i to j
# INF = float('inf') means no path exists between those nodes

INF = float('inf')

test_cases = [
    (
        4,
        [(0,1,2),(1,0,7),(1,2,3),(2,1,8),(2,3,2),(3,0,1),(3,1,5)],
        [[0,2,5,7],[6,0,3,5],[3,5,0,2],[1,3,6,0]],
        "4 nodes: classic example with multiple relaxations"
    ),
    (
        2,
        [(0,1,3),(1,0,5)],
        [[0,3],[5,0]],
        "2 nodes: bidirectional edges"
    ),
    (
        3,
        [(0,2,10),(0,1,1),(1,2,1)],
        [[0,1,2],[INF,0,1],[INF,INF,0]],
        "3 nodes: indirect path cheaper than direct (0→1→2=2 vs 0→2=10)"
    ),
    (
        3,
        [(0,1,5),(1,2,3),(0,2,4)],
        [[0,5,4],[INF,0,3],[INF,INF,0]],
        "3 nodes: direct path cheaper than indirect (0→2=4 vs 0→1→2=8)"
    ),
    (
        4,
        [(0,1,5),(2,3,3)],
        [[0,5,INF,INF],[INF,0,INF,INF],[INF,INF,0,3],[INF,INF,INF,0]],
        "disconnected: two isolated components, unreachable pairs stay INF"
    ),
    (
        1,
        [],
        [[0]],
        "single node: no edges"
    ),
]

passed = 0
for idx, (V, edges, expected, desc) in enumerate(test_cases, 1):
    result = floyd_warshall(V, edges)
    ok = result == expected
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  {desc}")
    if not ok:
        print(f"         result:   {result}")
        print(f"         expected: {expected}")

print(f"\n{passed}/{len(test_cases)} tests passed")