from utils.singleton import singleton
from complex.entities.simplicial_complex import SimplicialComplex
from complex.entities.miniplex import Miniplex


@singleton
class MiniplexFactory():

    def create_instance(self, complex: SimplicialComplex) -> Miniplex:
        miniplex = Miniplex(complex)
        # miniplex.make_nei()
        return miniplex

    def create_copy(self, miniplex: Miniplex) -> Miniplex:
        new_miniplex = Miniplex(miniplex.root)
        for v in miniplex.vertices:
            new_miniplex.add_vertex(v)

        for t in miniplex.triplets:
            new_miniplex.triplets.append(t)

        for q in miniplex.quartets:
            new_miniplex.quartets.append(t)

        return new_miniplex

    def create_miniplex(self,  complex: SimplicialComplex, vertices: list[int]):
        miniplex: Miniplex = Miniplex(complex)
        for v in vertices:
            miniplex.add_vertex(v)

        miniplex.add_triplets()
        miniplex.add_quartets()

        return miniplex
