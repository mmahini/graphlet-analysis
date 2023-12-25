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

        exact_graphlet_count = sum(len(v) for v in exact.gs.graphlets.values())
        if exact_graphlet_count != exact.gs.total_num_of_graphlets:
            print(f"Error, exact_graphlet_count: {exact_graphlet_count}, total_num_of_graphlets: {exact.gs.total_num_of_graphlets}")

        for i in range(len(exact.gs.graphlet_cnt)):
            j1 = exact.gs.graphlet_cnt[i]
            j2 = len(exact.gs.graphlets[i])
            if j1 != j2:
                print(f"prev exact: {i}= {j1}")
                print(f"new exact: {i}= {j2}")
                
    print(f"\ndone!!!")
