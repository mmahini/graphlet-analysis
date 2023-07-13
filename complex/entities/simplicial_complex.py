from complex.entities.topological_object import TopologicalObject


class SimplicialComplex(TopologicalObject):

    e: int
    vertices: set[int]
    triplets: set[tuple]
    quartets: set[tuple]
    mark: dict()
    nei: dict()

    def __init__(self):
        self.e = -1
        self.vertices = set()
        self.triplets = list[tuple]()
        self.quartets = list[tuple]()
        self.mark = dict()
        self.nei = dict()

    def init_marks(self):
        for v in self.vertices:
            self.mark[v] = False

    def init_nei(self):
        for v in self.vertices:
            self.nei[v] = set()

    def degree(self, v: int) -> int:
        return len(self.nei[v])

    def countE(self):
        if self.e != -1:
            return self.e

        self.e = 0
        for v in self.vertices:
            self.e += self.degree(v)
        self.e = int(self.e / 2)

        return self.e

    def write(self):
        e = self.countE()
        n = len(self.vertices)
        print(f"{e}\n{n}")

        for v in self.vertices:
            for u in self.nei[v]:
                if u > v:
                    print(f"{v} {u}")

        for t in self.triplets:
            print(f"{t[0]} {t[1]} {t[2]}")

        for q in self.quartets:
            print(f"{q[0]} {q[1]} {q[2]} {q[3]}")
