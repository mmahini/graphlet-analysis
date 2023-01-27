# Complete graph structure analysis

# Output:
#   1st: list of vertices and their adjacency list
#   2nd: graph connected components

from typing import List
from entities.graph import Graph
from connected_components import cc
from exact_graphlet_count import exact_graphlet_count

if __name__ == "__main__":
    g: Graph = Graph(0,0)
    g.load()

    print(g)

    print(cc(g))

    exact_graphlet_count(g)
