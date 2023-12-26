from complex.entities.simplicial_complex import SimplicialComplex
from complex.utils.simplex_utils import SimplexUtils


class Miniplex(SimplicialComplex):

    root: SimplicialComplex
    type: int = -1

    def __init__(self, complex: SimplicialComplex):
        super(SimplicialComplex, self).__init__()
        self.root = complex

        self.e = -1
        self.vertices = set()
        self.triplets = list[tuple]()
        self.quartets = list[tuple]()
        self.mark = dict()
        self.nei = dict()

    def add_vertex(self, v: int):
        self.vertices.add(v)
        self.mark[v] = False
        self.nei[v] = set()
        for u in self.vertices:
            if self.root.has_edge(v, u):
                self.nei[v].add(u)
                self.nei[u].add(v)

    def remove_vertex(self, v: int):
        self.vertices.remove(v)
        self.mark.pop(v)
        for u in self.nei[v]:
            self.nei[u].remove(v)
        self.nei.pop(v)

        new_triplets = list[tuple]()
        for t in self.triplets:
            if v not in t:
                new_triplets.append(t)
        self.triplets = new_triplets

        new_quartets = list[tuple]()
        for q in self.quartets:
            if v not in q:
                new_quartets.append(q)
        self.quartets = new_quartets

    def add_vertex_simplex(self, v: int):
        for t in self.root.triplets:
            if v in t:
                vertices = tuple(int(item) for item in t)
                if (set(vertices).issubset(self.vertices)):
                    self.triplets.append(t)

        for q in self.root.quartets:
            if v in q:
                vertices = tuple(int(item) for item in q)
                if (set(vertices).issubset(self.vertices)):
                    self.quartets.append(q)

    def add_triplets(self):
        for t in self.root.triplets:
            vertices = tuple(int(item) for item in t)
            if (set(vertices).issubset(self.vertices)):
                self.triplets.append(t)

    def add_quartets(self):
        for q in self.root.quartets:
            vertices = tuple(int(item) for item in q)
            if (set(vertices).issubset(self.vertices)):
                self.quartets.append(q)

    def get_type(self) -> int:
        if self.type == -1:
            self.type = SimplexUtils().calc_miniplex_type(self)
        return self.type

    def get_neighbor_vertices(self) -> set:
        neighbor_vertices = set()
        for v in self.vertices:
            for u in self.root.nei[v]:
                if u not in self.vertices:
                    neighbor_vertices.add(u)
        return neighbor_vertices

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

    def __eq__(self, other):
        if isinstance(other, Miniplex):
            return self.vertices == other.vertices
        return NotImplemented

    def __ne__(self, other):
        x = self.__eq__(other)
        if x is NotImplemented:
            return NotImplemented
        return not x
    
    def __hash__(self):
        return hash(tuple(sorted(self.vertices)))
