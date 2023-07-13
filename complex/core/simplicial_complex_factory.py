from utils.singleton import singleton
from complex.entities.simplicial_complex import SimplicialComplex


@singleton
class SimplicialComplexFactory():

    def create_instance(self) -> SimplicialComplex:
        return SimplicialComplex()

    def create_instance_with_n_vertices_from(self, n: int) -> SimplicialComplex:
        complex = self.create_instance()

        for i in range(n):
            complex.vertices.add(i)

        complex.init_marks()
        complex.init_nei()

        return complex

    # Load SimplcialComplex from input. n, e and each simplex is in separate line
    def load_from_cmd(self) -> SimplicialComplex:
        n = int(input())
        e = int(input())

        complex = self.create_instance_with_n_vertices_from(n)

        try:
            while (True):
                print("a")
                row: tuple = input().split(" ")
                if (len(row) == 2):
                    v = int(row[0])
                    u = int(row[1])
                    complex.nei[v].add(u)
                    complex.nei[u].add(v)
                elif (len(row) == 3):
                    complex.triplets.append(sorted(row))
                elif (len(row) == 4):
                    complex.quartets.append(sorted(row))
                else:
                    raise RuntimeError(
                        'more than 4 dimensions simplex is not supported'
                    )
        except EOFError as err:
            pass

        return complex
