#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

import time
from concurrent.futures import ThreadPoolExecutor
from graph.graph import Graph, GraphFactory
from algorithms.guise import Guise
from algorithms.gfd import EpsilonDelta, GfdUtils
from algorithms.exact import Exact


# Test guise graphlet count diff with exact count
def guise_error_calculation():
    n = int(input())
    p = float(input())

    graphlet_count_ed = EpsilonDelta([0.1, 0.05, 0.02, 0.01])
    vertex_graphlet_count_ed = EpsilonDelta([0.05, 0.02, 0.01, 0.005])
    vertex_orbit_count_ed = EpsilonDelta([0.01, 0.005, 0.002, 0.001])

    for i in range(20):
        print(f"run {i} ...")

        g: Graph = GraphFactory().get_random_instance(n, p)
        # print(g)

        exact: Exact = Exact(g)
        exact.run()

        guise: Guise = Guise(g)
        guise.run(10000, 10000)

        error_gc = GfdUtils().calc_graphlet_count_error(guise, exact)
        graphlet_count_ed.append_graphlet_count_error(error_gc)

        error_vgc = GfdUtils().calc_vertex_graphlet_count_error(guise, exact)
        vertex_graphlet_count_ed.append_vertex_count_error(error_vgc)

        error_voc = GfdUtils().calc_vertex_orbit_count_error(guise, exact)
        vertex_orbit_count_ed.append_vertex_count_error(error_voc)

    graphlet_count_ed.calc_delta()
    vertex_graphlet_count_ed.calc_delta()
    vertex_orbit_count_ed.calc_delta()

    print("\ngraphlet count")
    graphlet_count_ed.write()

    print("\nvertext graphlet count")
    vertex_graphlet_count_ed.write()

    print("\nvertext orbit count")
    vertex_orbit_count_ed.write()


if __name__ == "__main__":
    guise_error_calculation()
