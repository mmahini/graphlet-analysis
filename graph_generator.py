# Graph generator.
# Generate a random graph base on number of vertices and number of edges.

from typing import List
from graph import Graph

if __name__ == "__main__":
    n = int(input())
    e = int(input())

    g: Graph = Graph(0,0)
    g.gen(n, e)

    g.write()
