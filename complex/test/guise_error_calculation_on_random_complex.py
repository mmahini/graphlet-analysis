#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

import time
from concurrent.futures import ThreadPoolExecutor
from algorithms.epsilon_delta import EpsilonDelta
from complex.core.simplicial_complex_factory import SimplicialComplexFactory
from complex.entities.simplicial_complex import SimplicialComplex
from complex.algorithms.guise import Guise
from complex.algorithms.exact import Exact
from complex.utils.mfd import MfdUtils


# Test guise graphlet count diff with exact count
def guise_error_calculation():
    n = int(200)    # number of nodes in complex
    p = float(0.12)  # probability of vertices ,between 0 and 1
    t = float(0.80)  # probability of triplets ,between 0 and 1
    q = float(0.90)  # probability of quartets ,between 0 and 1

    epsilons = [0.0020, 0.0010, 0.0005, 0.0001]
    miniplex_count_ed = EpsilonDelta(epsilons)
    vertices_roles_ed = EpsilonDelta(epsilons)
    edges_roles_ed = EpsilonDelta(epsilons)
    triplets_roles_ed = EpsilonDelta(epsilons)
    
    centerality_epsilons = [0.0005, 0.0002, 0.0001, 0.00005]
    vertices_role_centerality_ed = EpsilonDelta(centerality_epsilons)
    edges_role_centerality_ed = EpsilonDelta(centerality_epsilons)
    triplets_role_centerality_ed = EpsilonDelta(centerality_epsilons)
    
    for i in range(2):
        complex: SimplicialComplex = SimplicialComplexFactory().create_random_instance(n, p, t, q)
        print(f"run {i} - #(edge,triple,tethra) = #({complex.countE()},{len(complex.triplets)},{len(complex.quartets)})")
        
        exact: Exact = Exact(complex)
        exact.run()
        exact.statistics.write()
    
        guise: Guise = Guise(complex)
        guise.run(1000, 1000)

        error_mc = MfdUtils().calc_miniplex_count_error(guise, exact)
        miniplex_count_ed.append_graphlet_count_error(error_mc)

        error_vr = MfdUtils().calc_vertices_role_error(guise, exact)
        vertices_roles_ed.append_vertex_graphlet_degree_centrality_error(error_vr)
        
        error_er = MfdUtils().calc_edges_role_error(guise, exact)
        edges_roles_ed.append_vertex_graphlet_degree_centrality_error(error_er)
        
        error_tr = MfdUtils().calc_triplets_role_error(guise, exact)
        triplets_roles_ed.append_vertex_graphlet_degree_centrality_error(error_tr)
        
        error_vrc = MfdUtils().calc_vertices_role_centerality_error(guise, exact)
        vertices_role_centerality_ed.append_vertex_graphlet_degree_centrality_error(error_vrc)
        
        error_erc = MfdUtils().calc_edges_role_centerality_error(guise, exact)
        edges_role_centerality_ed.append_vertex_graphlet_degree_centrality_error(error_erc)
        
        error_trc = MfdUtils().calc_triplets_role_centerality_error(guise, exact)
        triplets_role_centerality_ed.append_vertex_graphlet_degree_centrality_error(error_trc)

    print("calc diff")
    miniplex_count_ed.calc_delta()
    vertices_roles_ed.calc_delta()
    edges_roles_ed.calc_delta()
    triplets_roles_ed.calc_delta()
    vertices_role_centerality_ed.calc_delta()
    edges_role_centerality_ed.calc_delta()
    triplets_role_centerality_ed.calc_delta()

    print("\nminiplex count")
    miniplex_count_ed.write()

    print("\nvertices role")
    vertices_roles_ed.write()
    
    print("\nedges role")
    edges_roles_ed.write()
    
    print("\ntriplets role")
    triplets_roles_ed.write()
    
    print("\nvertices role centerality")
    vertices_role_centerality_ed.write()
    
    print("\nedges role centerality")
    edges_role_centerality_ed.write()
    
    print("\ntriplets role centerality")
    triplets_role_centerality_ed.write()


if __name__ == "__main__":
    guise_error_calculation()
