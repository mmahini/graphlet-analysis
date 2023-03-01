# Graph class and all of graph functions

from utils.singleton import singleton
from typing import List
from random import randint, random
from abc import ABC


class Graph(ABC):
    # Initialize an empty graph with n vertices and e edges
    # Initialize vertices neighborhood list (nei)
    # Initialize vertices marks for algorithms (mark)
    def __init__(self):
        self.e = -1
        self.vertices: set[int] = set()
        self.mark = dict()
        self.nei = dict()

    def countV(self):
        return len(self.vertices)

    def countE(self):
        if self.e != -1:
            return self.e

        self.e = 0
        for v in self.vertices:
            self.e += self.degree(v)
        self.e = int(self.e / 2)

        return self.e

    def init_marks(self):
        for v in self.vertices:
            self.mark[v] = False

    def init_nei(self):
        for v in self.vertices:
            self.nei[v] = set()

    def degree(self, v: int) -> int:
        return len(self.nei[v])

    # reset mark array to "False" for all vertices
    def reset_marks(self):
        for v in self.vertices:
            self.mark[v] = False

    def dfs(self, v: int) -> str:
        self.mark[v] = True
        for u in self.nei[v]:
            if not self.mark[u]:
                self.dfs(u)

    def is_connected(self) -> bool:
        if self.countE() < 1:
            return False

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

    def remove(self, v: int):
        self.vertices.remove(v)
        self.mark.pop(v)
        for u in self.nei[v]:
            self.nei[u].remove(v)
        self.nei.pop(v)

    # generate an string for graph based on it's adjacency list
    def __str__(self) -> str:
        n = len(self.vertices)
        e = self.countE()

        s = f"{n} {e}"
        if self.is_connected():
            s += " (is connected)"
        print(s)

        s: str = "Adjacency List:\n"
        for v in self.vertices:
            s = s + f"{v}: ["
            start: bool = True
            for u in self.nei[v]:
                if not start:
                    s = s + " "
                s = s + f"{u}"
                start = False
            s = s + "]\n"
        return s

    def has_edge(self, v: int, u: int) -> bool:
        return u in self.nei[v]

    # write graph to output. n, e and each edge is in separate line
    def write(self):
        n = len(self.vertices)
        e = self.countE()

        s = f"{n} {e}"
        if self.is_connected():
            s += " (is connected)"
        print(s)
        for v in self.vertices:
            for u in self.nei[v]:
                if u > v:
                    print(f"{v} {u}")

    # find number of edges in inductive sub-graph limited to "lst" as its vertices
    def subgraph_countE(self, lst: List) -> int:
        e: int = 0
        for i in lst:
            for j in lst:
                if i in self.nei[j]:
                    e = e + 1
        e = e / 2
        return e

    # find degree of vertex "v" in inductive sub-graph that's limited to "lst" as its vertices
    def subgraph_degree(self, v: int, lst: List) -> int:
        e: int = 0
        for i in lst:
            if i in self.nei[v]:
                e = e + 1
        return e


@singleton
class GraphFactory():

    def create_instance(self) -> Graph:
        return Graph()

    def create_instance_with_n_vertices_from(self, n: int) -> Graph:
        g = self.create_instance()

        for i in range(n):
            g.vertices.add(i)

        g.init_marks()
        g.init_nei()

        return g

    def create_instance_with_sets(self,  n, edges: set[list[int]]):
        g = self.create_instance_with_n_vertices_from(n)

        for e in edges:
            v = e[0]
            u = e[1]
            g.nei[v].add(u)
            g.nei[u].add(v)

        return g

    # generate a graph like G(n,p) : Erdos-Renyi
    # Graph has n vertices and every edge be with probability p
    def get_random_instance(self, n: int, p: float) -> Graph:
        g = self.create_instance_with_n_vertices_from(n)

        for v in g.vertices:
            for u in g.vertices:
                if v >= u:
                    continue
                if random() <= p:
                    g.nei[v].add(u)
                    g.nei[u].add(v)

        return g

    # load a graph from input. n, e and each edge is in separate line
    def load_graph_from_cmd(self) -> Graph:
        n = int(input())
        e = int(input())

        g = self.create_instance_with_n_vertices_from(n)

        for _ in range(e):
            v_str, u_str = input().split(" ")
            v = int(v_str)
            u = int(u_str)
            g.nei[v].add(u)
            g.nei[u].add(v)

        return g
