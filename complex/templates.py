
from utils.singleton import singleton
from complex.entities.simplicial_complex import SimplicialComplex
from complex.core.simplicial_complex_factory import SimplicialComplexFactory

NUM_OF_MINIPLEXES = 21


@singleton
class MiniplexTemplates():
    def __init__(self):
        self.initialized = False
        self.miniplexes: dict[int, SimplicialComplex] = dict()

    def list(self) -> dict[int, SimplicialComplex]:
        if self.initialized:
            return self.miniplexes

        self.miniplexes[0] = SimplicialComplexFactory().create_instance_with_set(
            2, [[0, 1]])
        self.miniplexes[1] = SimplicialComplexFactory().create_instance_with_set(
            3, [[0, 1], [1, 2]])
        self.miniplexes[2] = SimplicialComplexFactory().create_instance_with_set(
            3, [[0, 1], [1, 2], [0, 2]])
        self.miniplexes[3] = SimplicialComplexFactory().create_instance_with_set(
            3, [[0, 1], [0, 2], [1, 2], [0, 1, 2]])
        self.miniplexes[4] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [1, 2], [2, 3]])
        self.miniplexes[5] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [1, 2], [1, 3], [2, 3]])
        self.miniplexes[6] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        self.miniplexes[7] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3]])
        self.miniplexes[8] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        self.miniplexes[9] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 3], [1, 2, 3]])
        self.miniplexes[10] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [1, 2], [1, 3]])
        self.miniplexes[11] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 3], [1, 2], [2, 3]])
        self.miniplexes[12] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]])
        self.miniplexes[13] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
        self.miniplexes[14] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 3], [1, 2, 3]])
        self.miniplexes[15] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 3], [0, 2, 3], [1, 2, 3]])
        self.miniplexes[16] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]])
        self.miniplexes[17] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [1, 2, 3], [0, 1, 2, 3]])
        self.miniplexes[18] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 3], [1, 2, 3], [0, 1, 2, 3]])
        self.miniplexes[19] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2, 3]])
        self.miniplexes[20] = SimplicialComplexFactory().create_instance_with_set(
            4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3], [0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3], [0, 1, 2, 3]])

        return self.miniplexes
