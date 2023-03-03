from utils.singleton import singleton
from graph.graph import Graph
from graph.templates import GraphletTemplates, OrbitTemplates
from utils.graph import GraphUtils
from typing import List

NUM_OF_GRAPHLETS = 30
NUM_OF_ORBITS = 73


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
    def __init__(self, graph: Graph):
        super(SubGraphlet, self).__init__(graph)
        self.graphlet_type = -1

    def get_graphlet_type(self) -> int:
        if self.graphlet_type == -1:
            self.graphlet_type = GraphUtils().calc_graphlet_type(self)
        return self.graphlet_type

    def get_orbit_type(self, vertex: int) -> int:
        graphlet_type = self.get_graphlet_type()
        graphlet_of_graphlet_type = GraphletTemplates().list()[graphlet_type]
        orbit_types = OrbitTemplates().list()[graphlet_type]

        if len(orbit_types) == 1:
            return list(orbit_types)[0][0]

        for (o, u) in orbit_types:
            if GraphUtils().is_isomorph_vertex(self, vertex, graphlet_of_graphlet_type, u):
                return o

        raise ValueError('wrong calculation of orbit type')


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

    def create_subgraphlet(self,  graph: Graph, vertices: list[int]):
        sub_graphlet = SubGraphlet(graph)
        for v in vertices:
            sub_graphlet.add(v)
        return sub_graphlet
