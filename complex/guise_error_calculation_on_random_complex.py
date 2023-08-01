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
    n = int(20)    # number of nodes in complex
    p = float(0.26)  # probability of vertices ,between 0 and 1
    t = float(0.5)  # probability of triplets ,between 0 and 1
    q = float(0.5)  # probability of quartets ,between 0 and 1

    miniplex_count_ed = EpsilonDelta([0.1, 0.05, 0.02, 0.01])
    
    for i in range(10):
        complex: SimplicialComplex = SimplicialComplexFactory().create_random_instance(n, p, t, q)
        
        exact: Exact = Exact(complex)
        exact.run()
    
        guise: Guise = Guise(complex)
        guise.run(10000, 10000)

        error_mc = MfdUtils().calc_miniplex_count_error(guise, exact)
        miniplex_count_ed.append_graphlet_count_error(error_mc)

    print("calc diff")
    miniplex_count_ed.calc_delta()

    print("\nminiplex count")
    miniplex_count_ed.write()


if __name__ == "__main__":
    guise_error_calculation()
