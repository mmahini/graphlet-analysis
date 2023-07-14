from complex.graph import Graph
from complex.statistics import MiniplexStatistics
from complex.entities.simplicial_complex import SimplicialComplex
from abc import ABC


class MfdAglorithm(ABC):

    log: bool = False
    complex: SimplicialComplex
    statistics: MiniplexStatistics

    def __init__(self, complex: SimplicialComplex):
        self.complex = complex
        self.statistics: MiniplexStatistics = MiniplexStatistics(complex)
