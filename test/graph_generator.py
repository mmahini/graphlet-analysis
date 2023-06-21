#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

from typing import List
from graph.graph import Graph, GraphFactory

# Generate a random graph base on Erdos-Renyi.
if __name__ == "__main__":
    n = int(input())
    p = float(input())

    g: Graph = GraphFactory().get_random_instance(n, p)
    g.write()
