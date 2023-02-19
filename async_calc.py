from entities.graph import Graph, GraphFactory
from entities.graphlet import SubGraphletFactory, SubGraphlet
from entities.graphlet_templates import GraphletTemplates
from graph_algorithms.graph_utils import GraphUtils
from graph_algorithms.gfd_algorithm import EpsilonDelta
from guise.guise import Guise
from exact.exact_graphlet_count import Exact
from random import random
import asyncio


async def guise_error_calculation():
    n = int(input())
    e = int(input())

    epsilonDelta = EpsilonDelta()

    for i in range(0, 20):
        print(f"run {i} ...")
        async_calc(epsilonDelta)

    epsilonDelta.calc_delta()
    epsilonDelta.write()


async def async_calc(epsilonDelta: EpsilonDelta):
    factory = GraphFactory()
    g: Graph = factory.gen_instance(n, e)
    print(g)

    exact: Exact = Exact(g)
    exact.run()

    guise: Guise = Guise(g)
    guise.run(10000, 10000)

    error = epsilonDelta.calc_error(guise, exact)
    epsilonDelta.append_error(error)

if __name__ == "__main__":
    guise_error_calculation()
