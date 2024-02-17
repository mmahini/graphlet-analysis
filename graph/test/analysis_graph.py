from graph.graph import GraphFactory, Graph
from algorithms.exact import Exact
from graph.statistics import GraphletStatistics

if __name__ == '__main__':
    g: Graph = GraphFactory().load_graph_from_cmd()
    g.write()

    exact: Exact = Exact(g)
    exact.run()

    gs: GraphletStatistics = exact.gs
    gs.write()
