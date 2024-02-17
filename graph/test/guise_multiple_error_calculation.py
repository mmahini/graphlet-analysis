#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

from algorithms.exact import Exact
from algorithms.gfd import EpsilonDelta, GfdUtils
from algorithms.guise import Guise
from graph.graph import Graph, GraphFactory
from concurrent.futures import ThreadPoolExecutor
import time


num_of_running_alg = 3
stationary_steps = 10000
n_steps = 1000


def guise_error_calculation():
    n = int(input())
    p = float(input())

    ratio_list = [1, 2.5, 5, 10, 25]

    graphlet_count_ed_list: list[EpsilonDelta] = list()
    for r in ratio_list:
        graphlet_count_ed_list.append(EpsilonDelta([0.1, 0.05, 0.02, 0.01]))
    vertex_graphlet_count_ed_list: list[EpsilonDelta] = list()
    for r in ratio_list:
        vertex_graphlet_count_ed_list.append(EpsilonDelta([0.05, 0.02, 0.01, 0.005]))
    vertex_orbit_count_ed_list: list[EpsilonDelta] = list()
    for r in ratio_list:
        vertex_orbit_count_ed_list.append(EpsilonDelta([0.01, 0.005, 0.002, 0.001]))
    vertex_graphlet_degree_centrality_ed_list: list[EpsilonDelta] = list()
    for r in ratio_list:
        vertex_graphlet_degree_centrality_ed_list.append(EpsilonDelta([0.05, 0.02, 0.01, 0.005]))

    for i in range(num_of_running_alg):
        print(f"run {i} ...")

        g: Graph = GraphFactory().get_random_instance(n, p)

        print("calc exact")
        start = time.time()
        exact: Exact = Exact(g)
        exact.run()
        print(f"calc exact at {time.time() - start} seconds")

        for r in range(len(ratio_list)):
            print("calc exact")
            start = time.time()
            guise: Guise = Guise(g)
            steps = int(ratio_list[r] * n_steps)
            guise.run(stationary_steps, steps)
            print(f"calc guise with {steps} steps, at {time.time() - start} seconds")

            error_gc = GfdUtils().calc_graphlet_count_error(guise, exact)
            graphlet_count_ed_list[r].append_graphlet_count_error(error_gc)

            error_vgc = GfdUtils().calc_vertex_graphlet_count_error(guise, exact)
            vertex_graphlet_count_ed_list[r].append_vertex_count_error(error_vgc)

            error_voc = GfdUtils().calc_vertex_orbit_count_error(guise, exact)
            vertex_orbit_count_ed_list[r].append_vertex_count_error(error_voc)

            error_gdc = GfdUtils().calc_vertex_graphlet_degree_centrality_error(guise, exact)
            vertex_graphlet_degree_centrality_ed_list[r].append_vertex_graphlet_degree_centrality_error(error_gdc)


    for r in range(len(ratio_list)):
        print(f"\n--- ratio {ratio_list[r]} ---")
        
        graphlet_count_ed_list[r].calc_delta()
        vertex_graphlet_count_ed_list[r].calc_delta()
        vertex_orbit_count_ed_list[r].calc_delta()
        vertex_graphlet_degree_centrality_ed_list[r].calc_delta()

        print("\ngraphlet count")
        graphlet_count_ed_list[r].write()
        print("\nvertext graphlet count")
        vertex_graphlet_count_ed_list[r].write()
        print("\nvertext orbit count")
        vertex_orbit_count_ed_list[r].write()
        print("\nvertex graphlet degree centrality")
        vertex_graphlet_degree_centrality_ed_list[r].write()


if __name__ == "__main__":
    guise_error_calculation()
