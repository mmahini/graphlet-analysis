from utils.singleton import singleton
from complex.entities.miniplex import Miniplex


@singleton
class RoleUtils():
    
    def create_for_vertices(self) -> dict:
        d = dict()
        for i in (1, 3, 4, 6, 8, 11, 12, 15, 16, 17, 21, 22, 23, 28, 29, 32, 33, 34, 39, 40, 44, 45, 47, 49, 51, 52, 56, 57, 62, 63, 67, 70):
            d[i]= 0
        return d
    
    def create_for_edges(self) -> dict:
        d = dict()
        for i in (2, 5, 7, 9, 13, 14, 18, 19, 20, 24, 25, 26, 30, 31, 35, 36, 37, 41, 42, 46, 48, 50, 53, 54, 58, 59, 60, 64, 65, 68, 71):
            d[i]= 0
        return d

    def create_for_triplets(self) -> dict:
        d = dict()
        for i in (10, 27, 38, 43, 55, 61, 66, 69, 72):
            d[i]= 0
        return d
    