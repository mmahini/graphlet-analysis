# Graph class and all of graph functions
from utils.singleton import singleton

from typing import List
from random import randint

class Graph:
    # Initialize an empty graph with n vertices and e edges
    # Initialize vertices neighborhood list (nei)
    # Initialize vertices marks for algorithms (mark)
    def __init__(self, n : int = 0, e : int = 0):
        self.n = n
        self.e = e
        self.nei = list()
        self.mark = list()

        for _ in range(0, self.n):
            self.nei.append(set())
        for _ in range(0, self.n):
            self.mark.append(False)

    def has_edge(self, v : int, u : int) -> bool:
        return u in self.nei[v]

    # reset mark array to "False" for all vertices
    def reset_marks(self):
        for _ in range(0, self.n-len(self.mark)):
            self.mark.append(False)

        for i in range(0, self.n):
            self.mark[i] = False

    # generate an string for graph based on it's adjacency list
    def __str__(self) -> str:
        s: str = "Adjacency List:\n"
        for v in range(0, self.n):
            s = s + f"{v}: ["
            start : bool = True
            for u in self.nei[v]:
                if not start:
                    s = s + " "
                s = s + f"{u}"
                start = False
            s = s + "]\n"
        return s

    # write graph to output. n, e and each edge is in separate line
    def write(self):
        print(f"{self.n}\n{self.e}")
        for v in range(0,self.n):
            for u in self.nei[v]:
                if u > v:
                    print(f"{v} {u}")

    # load a graph from input. n, e and each edge is in separate line
    def load(self):
        self.n = int(input())
        self.e = int(input())

        for _ in range(0, self.n-len(self.nei)):
            self.nei.append(set())

        for _ in range(0, self.e):
            v_str, u_str = input().split(" ")
            v = int(v_str)
            u = int(u_str)
            self.nei[v].add(u)
            self.nei[u].add(v)

    # generate a graph with n vertices and e edges.
    # probability of selection of every edge is uniform.
    def gen(self, n: int, e: int):
        self.n = n
        self.e = e

        for _ in range(0, self.n-len(self.nei)):
            self.nei.append(set())

        i : int = 0
        while i < self.e:
            v = randint(0, self.n-1)
            u = randint(0, self.n-1)
            if v != u and v not in self.nei[u]:
                i += 1
                self.nei[v].add(u)
                self.nei[u].add(v)

    # find number of edges in inductive sub-graph limited to "lst" as its vertices
    def countE(self, lst: List) -> int:
        e : int = 0
        for i in lst:
            for j in lst:
                if i in self.nei[j]:
                    e = e + 1
        e = e / 2
        return e

    # find degree of vertex "v" in inductive sub-graph that's limited to "lst" as its vertices
    def degree(self, v: int, lst: List) -> int:
        e : int = 0
        for i in lst:
            if i in self.nei[v]:
                e = e + 1
        return e


@singleton
class GraphFactory():
    @staticmethod
    def get_instance() -> Graph:
        return Graph(0,0)
