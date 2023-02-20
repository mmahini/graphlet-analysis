import time
from concurrent.futures import ThreadPoolExecutor
from entities.graph import Graph, GraphFactory
from guise.guise import Guise
from graph_algorithms.gfd_algorithm import EpsilonDelta
from exact.exact_graphlet_count import Exact


def guise_error_calculation():
    n = int(input())
    e = int(input())

    epsilonDelta = EpsilonDelta()

    start_time = time.time()

    for i in range(0, 20):
        print(f"run {i} ...")
        factory = GraphFactory()
        g: Graph = factory.gen_instance(n, e)
        print(g)

        exact: Exact = Exact(g)
        exact.run()

        guise: Guise = Guise(g)
        guise.run(10000, 10000)

        error = epsilonDelta.calc_error(guise, exact)
        epsilonDelta.append_error(error)

    print(f"--- {time.time() - start_time:.5f} seconds ---\n\r")

    epsilonDelta.calc_delta()
    epsilonDelta.write()


if __name__ == "__main__":
    guise_error_calculation()
