#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

import time
from concurrent.futures import ThreadPoolExecutor
from algorithms.epsilon_delta import EpsilonDelta
from complex.core.simplicial_complex_factory import SimplicialComplexFactory
from complex.entities.simplicial_complex import SimplicialComplex
from complex.algorithms.guise import Guise
from complex.algorithms.gfd import GfdUtils
from complex.algorithms.exact import Exact


# Test guise graphlet count diff with exact count
def guise_error_calculation():
    complex: SimplicialComplex = SimplicialComplexFactory().load_from_cmd()

    miniplex_count_ed = EpsilonDelta([0.1, 0.05, 0.02, 0.01])

    print("calc exact")
    start = time.time()
    exact: Exact = Exact(g)
    exact.run()
    print(f"calc exact at {time.time() - start} seconds")
    
    total_average_gdc_list = list()
    
    for i in range(20):
        print(f"calc guise for {i}")
        start = time.time()
        guise: Guise = Guise(g)
        guise.run(10000, 10000)
        print(f"calc guise at {time.time() - start} seconds")

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

    print("calc diff")
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
