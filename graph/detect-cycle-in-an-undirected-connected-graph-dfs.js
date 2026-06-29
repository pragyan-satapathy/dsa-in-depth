function hasCycle(edges) {
  // build adjacency list
  let graph = {}
  for (let [u, v] of edges) {
    if (!graph[u]) graph[u] = [];
    if (!graph[v]) graph[v] = [];

    graph[u].push(v);
    graph[v].push(u);
  }

  let visited = new Set()
  let dfs = (node, parent) => {
    visited.add(node)
    for (let i of graph[node]) {
      if (!visited.has(i)) {
        return dfs(i, node)         // recurse on unvisited neighbor
      }
      else if (i != parent) {
        return true                 // visited and not parent → cycle
      }
    }
    return false
  }
  return dfs(0, null) ? true : false
}

module.exports = { hasCycle };
