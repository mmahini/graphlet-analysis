from entities.graph import Graph, GraphFactory
from exact.exact_graphlet_count import Exact

def exact_count():
    factory = GraphFactory()
    g: Graph = factory.load_graph_from_cmd()
    print(g)

    exact: Exact = Exact(g)
    exact.log = True
    exact.run()


if __name__ == "__main__":
    exact_count()
