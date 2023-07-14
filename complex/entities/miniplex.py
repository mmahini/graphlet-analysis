from complex.entities.simplicial_complex import SimplicialComplex
from complex.utils.simplex_utils import SimplexUtils


class Miniplex(SimplicialComplex):

    root: SimplicialComplex
    type: int = -1

    def __init__(self, complex: SimplicialComplex):
        super(SimplicialComplex, self).__init__()

    def addVertex(self, v: int):
        self.vertices.add(v)
        self.mark[v] = False
        self.nei[v] = set()
        for u in self.vertices:
            if self.root.has_edge(v, u):
                self.nei[v].add(u)
                self.nei[u].add(v)
                
    def get_type(self) -> int:
        if self.type == -1:
            self.type = SimplexUtils().calc_miniplex_type(self)
        return self.type
