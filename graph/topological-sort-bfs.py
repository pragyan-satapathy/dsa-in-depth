# question
# =====================
# Topological Sort - Kahn's Algorithm (BFS)
# Linear ordering of a DAG such that for every directed edge u→v, u comes before v.
#
# Approach (Kahn's Algorithm):
#   1. Compute in-degree of every node.
#   2. Push all nodes with in-degree 0 into a queue.
#   3. While queue is not empty:
#        - Pop node curr, add to result.
#        - For each neighbor of curr, decrement its in-degree.
#        - If in-degree becomes 0, push it into the queue.
#   4. Return result (already in topological order, no reversal needed).

from queue import Queue

def topo_sort(adj):
    # compute in-degree for every node
    indeg = [0] * len(adj)
    for a in adj:
        for v in a:
            indeg[v] += 1

    # enqueue all nodes with in-degree 0 (no dependencies)
    q = Queue()
    for i in range(len(indeg)):
        if indeg[i] == 0:
            q.put(i)

    res = []
    while q.qsize():
        curr = q.get()              # process node with no remaining deps
        res.append(curr)
        for i in adj[curr]:
            indeg[i] -= 1          # remove edge curr -> i
            if indeg[i] == 0:
                q.put(i)           # all deps satisfied, ready to process
    if len(res) != len(adj):
        print("Graph has a cycle, and topo sort is not possible.")
        return []
    return res                     # already in topological order (no reverse needed)



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
