def topo_sort(adj):
    visited = set()
    res = []
    def dfs(node):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:  # visit all unvisited neighbors first
                dfs(neighbor)
        res.append(node)                 # append after all descendants are done
    for i in range(len(adj)):
        if i not in visited:             # handle disconnected components(in disconnected graph)
            dfs(i)
    return res[::-1]                     # reverse → nodes with no deps come first


# test
# ============
def is_valid_topo(order, adj):
    pos = {node: i for i, node in enumerate(order)}
    for u in range(len(adj)):
        for v in adj[u]:
            if pos[u] > pos[v]:   # u must come before v
                return False
    return True


test_cases = [
    # adj list, num_nodes, description
    (
        [[], [], [3], [1], [0, 1], [0, 2]],
        "example from problem: 5->0,2 | 4->0,1 | 2->3 | 3->1"
    ),
    (
        [[1], [2], []],
        "simple chain: 0->1->2"
    ),
    (
        [[], [], [], []],
        "no edges: any order valid"
    ),
    (
        [[1, 2], [], [3], []],
        "0->1, 0->2->3"
    ),
    (
        [[2], [0], [], [1]],
        "3->1->0->2"
    ),
    (
        [[], [0], [0], [1, 2]],
        "3->1->0 and 3->2->0"
    ),
]

passed = 0
for idx, (adj, desc) in enumerate(test_cases, 1):
    result = topo_sort(adj)
    ok = is_valid_topo(result, adj)
    passed += ok
    status = "PASS" if ok else "FAIL"
    print(f"Test {idx:2}: {status}  order={result}")
    print(f"         {desc}")

print(f"\n{passed}/{len(test_cases)} tests passed")
