from utils.singleton import singleton
from complex.templates import MiniplexTemplates
from complex.entities.simplicial_complex import SimplicialComplex


@singleton
class SimplexUtils():

    def dimension(self, simplex) -> int:
        return len(simplex)-1

    def degree_map(self, complex: SimplicialComplex) -> dict[int, int]:
        res: dict[int, int] = dict()
        for v in complex.vertices:
            deg = complex.degree(v)
            if res.get(deg) != None:
                res[deg] += 1
            else:
                res[deg] = 1
        return res

    def is_equal_degree_map(self, complex1: SimplicialComplex, complex2: SimplicialComplex) -> bool:
        degree_map1 = self.degree_map(complex1)
        degree_map2 = self.degree_map(complex2)

        for (d, d_n) in degree_map1.items():
            if degree_map2.get(d) == None or degree_map2[d] != d_n:
                return False

        for (d, d_n) in degree_map2.items():
            if degree_map1.get(d) == None or degree_map1[d] != d_n:
                return False

        return True

    def calc_miniplex_type(self, complex: SimplicialComplex) -> int:
        miniplex_templates = MiniplexTemplates().list()
        for (k, miniplex) in miniplex_templates.items():
            if self.is_equal_degree_map(complex, miniplex):
                # handle special cases
                # if k == 11:
                #     return self.get_type_between_graphlet_11_12(g)
                # if k == 24:
                #     return self.get_type_between_graphlet_24_27(g)
                return k

        print(g)
        raise ValueError('wrong calculation of miniplex type')
