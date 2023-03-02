#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

from graph.graph import Graph, GraphFactory
from algorithms.exact import Exact

# Test exact graphlet count calculation based on random generated graph
if __name__ == "__main__":
    g: Graph = GraphFactory().load_graph_from_cmd()
    print(g)

    exact: Exact = Exact(g)
    exact.log = True
    exact.run()
