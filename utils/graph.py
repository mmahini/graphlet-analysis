from graph.graph import Graph
from graph.templates import GraphletTemplates
from utils.singleton import singleton


@singleton
class GraphUtils():
    def degree_map(self, g: Graph) -> dict[int, int]:
        res: dict[int, int] = dict()
        for v in g.vertices:
            deg = g.degree(v)
            if res.get(deg) != None:
                res[deg] += 1
            else:
                res[deg] = 1
        return res

    def is_equal_degree_map(self, g1: Graph, g2: Graph) -> bool:
        d_map1 = self.degree_map(g1)
        d_map2 = self.degree_map(g2)

        for (d, d_n) in d_map1.items():
            if d_map2.get(d) == None or d_map2[d] != d_n:
                return False

        for (d, d_n) in d_map2.items():
            if d_map1.get(d) == None or d_map1[d] != d_n:
                return False

        return True

    def calc_graphlet_type(self, g : Graph) -> int:
        graphlet_templates = GraphletTemplates().list()
        for (k, graphlet) in graphlet_templates.items():
            if self.is_equal_degree_map(g, graphlet):
                # handle special cases
                if k == 11:
                    return self.get_type_between_graphlet_11_12(g)
                if k == 24:
                    return self.get_type_between_graphlet_24_27(g)
                return k
        
        print(g)
        raise ValueError('wrong calculation of graphlet type')

    def is_isomorph(self, g1: Graph, g2: Graph) -> bool:
        if not self.is_equal_degree_map(g1, g2):
            return False

        if g1.countE() == 6:  # graphlet number 24 or 27
            return self.get_type_between_graphlet_24_27(g1) == self.get_type_between_graphlet_24_27(g2)
        if g1.countE() == 5:  # graphlet number 11 or 12
            return self.get_type_between_graphlet_11_12(g1) == self.get_type_between_graphlet_11_12(g2)

        return True

    def is_isomorph_vertex(self, g1: Graph, v1: int, g2: Graph,  v2: int) -> bool:
        if g1.degree(v1) != g2.degree(v2):
            return False

        v1_nei_degrees = {g1.degree(w) for w in g1.nei[v1]}
        v2_nei_degrees = {g2.degree(w) for w in g2.nei[v2]}

        for x in v1_nei_degrees:
            if x not in v2_nei_degrees:
                return False

        return True

    def get_type_between_graphlet_11_12(self, g: Graph) -> int:
        for v in g.vertices:
            if g.degree(v) == 3:
                for u in g.vertices:
                    if g.degree(u) == 1:
                        if v in g.nei[u]:
                            return 12
                        else:
                            return 11

    def get_type_between_graphlet_24_27(self, g: Graph) -> int:
        for v in g.vertices:
            if g.degree(v) == 3:
                for u in g.vertices:
                    if u == v:
                        continue
                    if g.degree(u) == 3:
                        if v in g.nei[u]:
                            return 27
                        else:
                            return 24

        return -1
