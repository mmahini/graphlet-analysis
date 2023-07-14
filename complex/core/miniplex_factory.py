from utils.singleton import singleton
from complex.entities.simplicial_complex import SimplicialComplex
from complex.entities.miniplex import Miniplex


@singleton
class MiniplexFactory():

    def create_instance(self, complex: SimplicialComplex) -> Miniplex:
        miniplex = Miniplex(complex)
        miniplex.make_nei()
        return miniplex

    def create_copy(self, miniplex: Miniplex) -> Miniplex:
        new_miniplex = Miniplex(miniplex.root)
        for v in miniplex.vertices:
            new_miniplex.add(v)
        return new_miniplex

    def create_miniplex(self,  complex: SimplicialComplex, vertices: list[int]):
        miniplex = Miniplex(complex)
        for v in vertices:
            miniplex.vertices.add(v)
            miniplex.mark[v] = False
            miniplex.nei[v] = set()
            for u in miniplex.vertices:
                if miniplex.root.has_edge(v, u):
                    miniplex.nei[v].add(u)
                    miniplex.nei[u].add(v)
        
        for t in complex.triplets:
            if(set(t).issubset(miniplex.vertices)):
                miniplex.triplets.append(t)
                
        for q in complex.quartets:
            if(set(q).issubset(miniplex.vertices)):
                miniplex.quartets.append(t)
        
        return miniplex
