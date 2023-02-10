from entities.graph import Graph, GraphFactory
from entities.graphlet import SubGraphletFactory, SubGraphlet
from entities.graphlet_templates import GraphletTemplates
from graph_algorithms.graph_utils import GraphUtils
from guise.guise import guise_algorithm

def test1():
    factory = GraphFactory()
    g : Graph = factory.load_graph_from_cmd()
    print(g)

    gl : SubGraphlet = SubGraphletFactory().get_instance(g)
    gl.add(2)
    gl.add(3)
    gl.add(4)
    gl.add(5)
    print(gl)

def test2():
    n = int(input())
    e = int(input())

    factory = GraphFactory()
    g : Graph = factory.gen_instance(n, e)
    g.write()

def test3():
    graphlet_templates = GraphletTemplates().list()
    for (k, graphlet) in graphlet_templates.items():
        print(f"{k} ----------------")
        print(graphlet)

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
    g : Graph = factory.load_graph_from_cmd()
    print(g)

    guise_algorithm(g, 0, 10)

if __name__ == "__main__":
    test_guise()