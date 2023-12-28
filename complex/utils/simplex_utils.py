from utils.singleton import singleton
from complex.templates import MiniplexTemplates
from complex.entities.simplicial_complex import SimplicialComplex

WRONG_MINIPLEX_TYPE = -1


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
        type = WRONG_MINIPLEX_TYPE
        templates = MiniplexTemplates().list()
        for (k, miniplex) in templates.items():
            if self.is_equal_degree_map(complex, miniplex):
                # handle special cases
                if k == 2:
                    type = self.calc_miniplex_type_between_2_3(complex)
                elif k == 5:
                    type = self.calc_miniplex_type_between_5_6(complex)
                elif k == 7:
                    type = self.calc_miniplex_type_between_7_9(complex)
                elif k == 12:
                    type = self.calc_miniplex_type_between_12_20(complex)
                else:
                    type = k
                break

        if (type == WRONG_MINIPLEX_TYPE):
            complex.write()
            raise ValueError('wrong calculation of miniplex type')
        else:
            return type

    def calc_miniplex_type_between_2_3(self, complex: SimplicialComplex) -> int:
        if len(complex.triplets) == 0:
            return 2
        elif len(complex.triplets) == 1:
            return 3
        else:
            return WRONG_MINIPLEX_TYPE

    def calc_miniplex_type_between_5_6(self, complex: SimplicialComplex) -> int:
        if len(complex.triplets) == 0:
            return 5
        elif len(complex.triplets) == 1:
            return 6
        else:
            return WRONG_MINIPLEX_TYPE

    def calc_miniplex_type_between_7_9(self, complex: SimplicialComplex) -> int:
        if len(complex.triplets) == 0:
            return 7
        elif len(complex.triplets) == 1:
            return 8
        elif len(complex.triplets) == 2:
            return 9
        else:
            return WRONG_MINIPLEX_TYPE

    def calc_miniplex_type_between_12_20(self, complex: SimplicialComplex) -> int:
        if len(complex.quartets) == 0:
            if len(complex.triplets) == 0:
                return 12
            if len(complex.triplets) == 1:
                return 13
            elif len(complex.triplets) == 2:
                return 14
            elif len(complex.triplets) == 3:
                return 15
            elif len(complex.triplets) == 4:
                return 16
        elif len(complex.quartets) == 1:
            if len(complex.triplets) == 1:
                return 17
            elif len(complex.triplets) == 2:
                return 18
            elif len(complex.triplets) == 3:
                return 19
            elif len(complex.triplets) == 4:
                return 20

        return WRONG_MINIPLEX_TYPE
