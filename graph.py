from typing import List
from random import randint

class Graph:
    def __init__(self, n: int, e: int):
        self.n = n
        self.e = e
        self.nei = list()
        self.mark = list()

        for _ in range(0, self.n):
            self.nei.append(set())
        for _ in range(0, self.n):
            self.mark.append(False)

    def reset_marks(self):
        for _ in range(0, self.n-len(self.mark)):
            self.mark.append(False)

        for i in range(0, self.n):
            self.mark[i] = False

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

    def write(self):
        print(f"{self.n}\n{self.e}")
        for v in range(0,self.n):
            for u in self.nei[v]:
                if u > v:
                    print(f"{v} {u}")

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

    def gen(self):
        self.n = int(input())
        self.e = int(input())

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