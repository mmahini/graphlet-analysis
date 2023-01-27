from utils.singleton import singleton
from abc import ABC
from typing import List

from entities.graph import Graph

NUM_OF_GRAPHLETS = 30

class InducedSubGraph(ABC):
    def __init__(self, graph: Graph):
        self.vertices : set[int] = set()
        self.graph = graph

        self.mark = dict()
        for v in self.vertices:
            self.mark[v] = False

        self.nei = dict()
        for v in self.vertices:
            self.nei[v] = set()

    def make_nei(self):
        for v in self.vertices:
            for u in self.vertices:
                if self.graph.has_edge(v,u):
                    self.nei[v].add(u)

    def get_neighbor_vertices(self, graph: Graph) -> set:
        neighbor_vertices = set()
        for v in self.vertices:
            for u in graph.nei[v]:
                if u not in self.vertices:
                    neighbor_vertices.add(u)
        return neighbor_vertices

    def dfs(self, v: int) -> str:
        self.mark[v] = True
        for u in self.nei[v]:
            if not self.mark[u]:
                self.dfs(u)

    def reset_marks(self):
        for v in self.vertices:
            self.mark[v] = False

    def is_connected(self) -> bool:
        self.reset_marks()
        start = -1
        for v in self.vertices:
            start = v
            break

        self.dfs(start)
        for v in self.vertices:
            if not self.mark[v]:
                return False
        return True

    def add(self, v: int):
        self.vertices.add(v)
        self.mark[v] = False
        self.nei[v] = set()
        for u in self.vertices:
            if self.graph.has_edge(v,u):
                self.nei[v].add(u)
                self.nei[u].add(v)

    
    def remove(self, v: int):
        self.vertices.remove(v)
        self.mark.remove(v)
        for u in self.nei[v]:
            self.nei[u].remove(v)
        self.nei.remove(v)

    def write(self):
        s = "{"
        first : bool = True
        for v in self.vertices:
            if not first:
                s = s + ", "
            s = s + f"{v}"
            first = False
        s = s + "}"
        if self.is_connected():
            s = s + " (is connected)"
        print(s)

    def write_all(self):
        self.write()
        s = "nei: {"
        for v in self.vertices:
            s += f" {v}: ["
            first : bool = True
            for u in self.nei[v]:
                if not first:
                    s = s + ", "
                s = s + f"{u}"
                first = False
            s += "] "
        s = s + "}"
        print(s)


class SubGraphlet(InducedSubGraph): 
    def get_graphlet_type() -> int:
        # TODO
        return 0

@singleton
class SubGraphletFactory():
    @staticmethod
    def get_instance(g: Graph) -> SubGraphlet:
        sub_graphlet = SubGraphlet(g)
        sub_graphlet.make_nei()
        return sub_graphlet

    @staticmethod
    def get_copy(sub_graphlet: SubGraphlet) -> SubGraphlet:
        new_graphlet : SubGraphlet(sub_graphlet.graph)
        for v in sub_graphlet.vertices:
            new_graphlet.add(v)
        return new_graphlet
