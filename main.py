from entities.graph import Graph, GraphFactory
from entities.graphlet import SubGraphletFactory, SubGraphlet
from entities.graphlet_templates import GraphletTemplates
from graph_algorithms.graph_utils import GraphUtils
from graph_algorithms.gfd_algorithm import EpsilonDelta
from guise.guise import Guise
from exact.exact_graphlet_count import Exact
from random import random


def generate_random_graph():
    print("input vertices: ")
    n = int(input())
    print("input edges: ")
    e = int(input())

    factory = GraphFactory()
    g: Graph = factory.gen_instance(n, e)
    g.write()


def test_graphlet_generate():
    factory = GraphFactory()
    g: Graph = factory.load_graph_from_cmd()
    print(g)

    gl: SubGraphlet = SubGraphletFactory().get_instance(g)
    gl.add(2)
    gl.add(3)
    gl.add(4)
    gl.add(5)
    print(gl)


def test_graph_templates():
    graphlet_templates = GraphletTemplates().list()
    for (k, graphlet) in graphlet_templates.items():
        print(f"[{k}] -> {GraphUtils().degree_map(graphlet)}")

    count = 0
    for (k1, g1) in graphlet_templates.items():
        for (k2, g2) in graphlet_templates.items():
            if GraphUtils().is_isomorph(g1, g2):
                count += 1
    print(f"{count} should be 30.")


def test_guise():
    factory = GraphFactory()
    g: Graph = factory.load_graph_from_cmd()
    print(g)

    guise: Guise = Guise(g)
    guise.run(100000, 500000)


def exact_count():
    factory = GraphFactory()
    g: Graph = factory.load_graph_from_cmd()
    print(g)

    exact: Exact = Exact(g)
    exact.run()


def guise_error_calculation():
    n = int(input())
    e = int(input())

    epsilonDelta = EpsilonDelta()

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

    epsilonDelta.calc_delta()
    epsilonDelta.write()


if __name__ == "__main__":
    guise_error_calculation()
