# Find and print connected components in input graph.
# Output : every line is the list of vertices of one component.

from typing import List
from graph.graph import Graph


def dfs(g: Graph, v: int) -> str:
    g.mark[v] = True
    dfs_str: str = str(v)
    for u in g.nei[v]:
        if not g.mark[u]:
            dfs_str = dfs_str + " " + dfs(g, u)
    return dfs_str


def cc(g: Graph) -> str:
    g.reset_marks()
    cc_str: str = "Connected Components:\n"
    for i in range(g.n):
        if not g.mark[i]:
            cc_str = cc_str + dfs(g, i) + "\n"
    return cc_str


if __name__ == "__main__":
    g: Graph = Graph(0, 0)
    g.load()

    print(cc(g))
