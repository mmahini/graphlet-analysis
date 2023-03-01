#!/usr/bin/env python3

from graph.graph import Graph, GraphFactory
from algorithms.guise import Guise

# Test guise graphlet count calculation based on random generated graph
if __name__ == "__main__":
    factory = GraphFactory()
    g: Graph = factory.load_graph_from_cmd()
    print(g)

    guise: Guise = Guise(g)
    guise.log = True
    guise.run(100000, 500000)
