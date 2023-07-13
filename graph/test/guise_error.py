#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

import time
from concurrent.futures import ThreadPoolExecutor
from algorithms.epsilon_delta import EpsilonDelta
from graph.graph import Graph, GraphFactory
from graph.algorithms.guise import Guise
from graph.algorithms.gfd import GfdUtils
from graph.algorithms.exact import Exact


# Test guise graphlet count diff with exact count
def guise_error_calculation():
    n = int(input())
    p = float(input())

    graphlet_count_ed = EpsilonDelta([0.1, 0.05, 0.02, 0.01])
    vertex_graphlet_count_ed = EpsilonDelta([0.05, 0.02, 0.01, 0.005])
    vertex_orbit_count_ed = EpsilonDelta([0.01, 0.005, 0.002, 0.001])
    vertex_graphlet_degree_centrality_ed = EpsilonDelta([0.05, 0.02, 0.01, 0.005])

    total_average_gdc_list = list()

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

        error_gdc = GfdUtils().calc_vertex_graphlet_degree_centrality_error(guise, exact)
        vertex_graphlet_degree_centrality_ed.append_vertex_graphlet_degree_centrality_error(error_gdc)
        
        average_gdc = sum(exact.gs.vertex_gdc.values()) / len(exact.gs.vertex_gdc.values())
        total_average_gdc_list.append(average_gdc)

    graphlet_count_ed.calc_delta()
    vertex_graphlet_count_ed.calc_delta()
    vertex_orbit_count_ed.calc_delta()
    vertex_graphlet_degree_centrality_ed.calc_delta()

    print("\ngraphlet count")
    graphlet_count_ed.write()

    print("\nvertext graphlet count")
    vertex_graphlet_count_ed.write()

    print("\nvertext orbit count")
    vertex_orbit_count_ed.write()
    
    print("\nvertex graphlet degree centrality")
    vertex_graphlet_degree_centrality_ed.write()
    
    total_average_gdc = sum(total_average_gdc_list) / len(total_average_gdc_list)
    print(f"\ntotal average gdc:    {total_average_gdc}")


if __name__ == "__main__":
    guise_error_calculation()
