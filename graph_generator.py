# Graph generator.
# Generate a random graph base on number of vertices and number of edges.

from typing import List
from entities.graph import Graph, GraphFactory

if __name__ == "__main__":
    n = int(input())
    e = int(input())

    factory = GraphFactory()
    g: Graph = factory.gen_instance(n, e)
    g.write()

