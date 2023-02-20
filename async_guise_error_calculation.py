import asyncio
import time
import os

from concurrent.futures import ThreadPoolExecutor
from entities.graph import Graph, GraphFactory
from guise.guise import Guise
from graph_algorithms.gfd_algorithm import EpsilonDelta
from exact.exact_graphlet_count import Exact

epsilonDelta = EpsilonDelta()
num_of_running_alg = 20
num_of_graph_v = 0
num_of_graph_e = 0

def calc_guise_error(num_of_run=0):
    print(f"run {num_of_run} ...")

    factory = GraphFactory()
    g: Graph = factory.gen_instance(num_of_graph_v, num_of_graph_e)
    # print(g)

    exact: Exact = Exact(g)
    exact.run()

    guise: Guise = Guise(g)
    guise.run(10000, 10000)

    error = epsilonDelta.calc_error(guise, exact)
    epsilonDelta.append_error(error)


async def parallel_calculation():
    executor = ThreadPoolExecutor(max_workers=os.cpu_count() - 1)
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(
        executor,
        calc_guise_error,
        i) for i in range(0, num_of_running_alg)]

    await asyncio.gather(*futures)


async def do_calculation():
    num_of_graph_v = int(input())
    num_of_graph_e = int(input())

    start_time = time.time()
    await parallel_calculation()

    print(f"--- {time.time() - start_time:.5f} seconds ---\n\r")

    epsilonDelta.calc_delta()
    epsilonDelta.write()


if __name__ == "__main__":
    asyncio.run(do_calculation())
