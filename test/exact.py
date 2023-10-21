#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

import time
from graph.graph import Graph, GraphFactory
from algorithms.exact import Exact

# Test exact graphlet count calculation based on random generated graph
if __name__ == "__main__":
    n = int(input())
    p = float(input())

    for i in range(10):
        print(f"run {i} ...")

        g: Graph = GraphFactory().get_random_instance(n, p)

        print("calc exact")
        start = time.time()
        exact: Exact = Exact(g)
        exact.run()
        print(f"calc exact at {time.time() - start} seconds")

    print(f"\ndone!!!")
