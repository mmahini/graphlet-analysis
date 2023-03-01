#!/usr/bin/env python3

from typing import List
from graph.graph import Graph, GraphFactory
from graph.graphlet import SubGraphlet, SubGraphletFactory

# Generate random graphlets base on Erdos-Renyi random Graph.
if __name__ == "__main__":
    factory = GraphFactory()
    g: Graph = factory.load_graph_from_cmd()
    print(g)

    gl: SubGraphlet = SubGraphletFactory().get_instance(g)
    gl.add(2)
    gl.add(3)
    gl.add(4)
    gl.add(5)
    print(gl)
