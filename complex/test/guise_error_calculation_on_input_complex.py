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
    complex: SimplicialComplex = SimplicialComplexFactory().load_from_cmd()

    miniplex_count_ed = EpsilonDelta([0.0250, 0.0100, 0.0075, 0.0050])

    print("calc exact")
    start = time.time()
    exact: Exact = Exact(complex)
    exact.run()
    print('---------- exact -------------')
    exact.statistics.write()
    exact.statistics.write_roles()
    print('-----------------------')
    # print(f"calc exact at {time.time() - start} seconds")
    
    for i in range(1):
        # print(f"calc guise for {i}")
        start = time.time()
        guise: Guise = Guise(complex)
        guise.run(1000, 1000)
        print('---------- guise -------------')
        guise.statistics.write()
        print('-----------------------')
        # print(f"calc guise at {time.time() - start} seconds")

        error_mc = MfdUtils().calc_miniplex_count_error(guise, exact)
        miniplex_count_ed.append_graphlet_count_error(error_mc)

    print("calc diff")
    miniplex_count_ed.calc_delta()

    print("\nminiplex count")
    miniplex_count_ed.write()


if __name__ == "__main__":
    guise_error_calculation()
