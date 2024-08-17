from utils.singleton import singleton
from complex.entities.miniplex import Miniplex


@singleton
class RoleUtils():
    
    VERTICES = (1, 3, 4, 6, 8, 11, 12, 15, 16, 17, 21, 22, 23, 28, 29, 32, 33, 34, 39, 40, 44, 45, 47, 49, 51, 52, 56, 57, 62, 63, 67, 70)
    EDGES = (2, 5, 7, 9, 13, 14, 18, 19, 20, 24, 25, 26, 30, 31, 35, 36, 37, 41, 42, 46, 48, 50, 53, 54, 58, 59, 60, 64, 65, 68, 71)
    TRIPLETS = (10, 27, 38, 43, 55, 61, 66, 69, 72)
    
    def create_for_vertices(self) -> dict:
        d = dict()
        for i in self.VERTICES:
            d[i]= 0
        return d
    
    def create_for_edges(self) -> dict:
        d = dict()
        for i in self.EDGES:
            d[i]= 0
        return d

    def create_for_triplets(self) -> dict:
        d = dict()
        for i in self.TRIPLETS:
            d[i]= 0
        return d
    
    def vertices_coefficient(self, role) -> int:
        if role in (1, 11, 12, 15, 16, 17, 21, 22, 23):
            return 2
        elif role in (32, 33, 34, 39, 40, 41):
            return 12
        else:
            return 1
        
    def edges_coefficient(self, role) -> int:
        if role in (2, 13, 14, 18, 19, 20, 24, 25, 26):
            return 2
        elif role in (30, 31, 35, 36, 37, 41, 42):
            return 12
        else:
            return 1
    
    def triplets_coefficient(self, role) -> int:
        if role in (10,):
            return 3
        elif role in (27,):
            return 8
        elif role in (38, 43, 55, 61, 66, 69, 72):
            return 24
        else:
            return 1
    