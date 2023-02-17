from utils.singleton import singleton
from entities.graph import Graph
from graph_algorithms.graph_utils import GraphUtils
from entities.graphlet_templates import GraphletTemplates
from typing import List

from entities.graph import Graph

NUM_OF_GRAPHLETS = 30


class InducedSubGraph(Graph):
    def __init__(self, graph: Graph):
        super(InducedSubGraph, self).__init__()

        self.graph = graph
        self.init_marks()
        self.init_nei()

    def make_nei(self):
        for v in self.vertices:
            for u in self.vertices:
                if self.graph.has_edge(v, u):
                    self.nei[v].add(u)

    def get_neighbor_vertices(self) -> set:
        neighbor_vertices = set()
        for v in self.vertices:
            for u in self.graph.nei[v]:
                if u not in self.vertices:
                    neighbor_vertices.add(u)
        return neighbor_vertices

    def add(self, v: int):
        self.vertices.add(v)
        self.mark[v] = False
        self.nei[v] = set()
        for u in self.vertices:
            if self.graph.has_edge(v, u):
                self.nei[v].add(u)
                self.nei[u].add(v)


class SubGraphlet(InducedSubGraph):
    def get_graphlet_type(self) -> int:
        graphlet_templates = GraphletTemplates().list()
        for (k, graphlet) in graphlet_templates.items():
            if GraphUtils().is_equal_degree_map(self, graphlet):
                return k
        return -1


@singleton
class SubGraphletFactory():
    def get_instance(self, g: Graph) -> SubGraphlet:
        sub_graphlet = SubGraphlet(g)
        sub_graphlet.make_nei()
        return sub_graphlet

    def get_copy(self, sub_graphlet: SubGraphlet) -> SubGraphlet:
        new_graphlet = SubGraphlet(sub_graphlet.graph)
        for v in sub_graphlet.vertices:
            new_graphlet.add(v)
        return new_graphlet
