from random import random
from utils.singleton import singleton
from complex.entities.simplicial_complex import SimplicialComplex


@singleton
class SimplicialComplexFactory():

    def create_instance(self) -> SimplicialComplex:
        return SimplicialComplex()

    def create_instance_with_n_vertices(self, n: int) -> SimplicialComplex:
        complex = self.create_instance()

        for i in range(n):
            complex.vertices.add(i)

        complex.init_marks()
        complex.init_nei()

        return complex

    def create_instance_with_set(self,  n, simplexes: set[list[int]]):
        complex = self.create_instance_with_n_vertices(n)

        for s in simplexes:
            if len(s) == 2:
                v = s[0]
                u = s[1]
                complex.nei[v].add(u)
                complex.nei[u].add(v)
            elif len(s) == 3:
                complex.triplets.append(sorted(s))
            elif len(s) == 4:
                complex.quartets.append(sorted(s))
            else:
                raise RuntimeError(
                    'more than 4 dimensions simplex is not supported'
                )

        return complex

    # create a new instance of a complex randomly
    # @parameter n: number of nodes in complex
    # @parameter p: probability of vertices ,between 0 and 1
    # @parameter t: probability of triplets ,between 0 and 1
    # @parameter q: probability of quartets ,between 0 and 1
    def create_random_instance(self, n: int, p: float, t: float, q: float) -> SimplicialComplex:
        complex = self.create_instance_with_n_vertices(n)

        for i in range(0, n):
            for j in range(i + 1, n):
                # for i,j
                if random() <= p:
                    complex.add_vertices([i, j])
                    complex.add_neighbors([[i, j]])

        for i in range(0, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # for i,j,k
                    if (j in complex.nei[i]) and (k in complex.nei[i]) and (j in complex.nei[k]):
                        if random() <= t:
                            complex.triplets.append([i, j, k])
                    for w in range(k + 1, n):
                        if (j in complex.nei[i]):
                            if (k in complex.nei[i]):
                                if (j in complex.nei[w]) and (k in complex.nei[w]):
                                    if random() <= q:
                                        complex.quartets.append([i, j, k, w])
                            elif (w in complex.nei[i]):
                                if (j in complex.nei[k]) and (w in complex.nei[k]):
                                    if random() <= q:
                                        complex.quartets.append([i, j, k, w])
                        elif (k in complex.nei[i]) and (w in complex.nei[i]):
                            if (w in complex.nei[j]) and (k in complex.nei[j]):
                                if random() <= q:
                                    complex.quartets.append([i, j, k, w])

        return complex

    # Load SimplcialComplex from input. n, e and each simplex is in separate line
    def load_from_cmd(self) -> SimplicialComplex:
        n = int(input())
        e = int(input())

        complex = self.create_instance_with_n_vertices(n)

        try:
            while (True):
                row: tuple = input().split(" ")
                if (len(row) == 2):
                    v = int(row[0])
                    u = int(row[1])
                    complex.nei[v].add(u)
                    complex.nei[u].add(v)
                elif (len(row) == 3):
                    complex.triplets.append(sorted(tuple(int(row_item) for row_item in row)))
                elif (len(row) == 4):
                    complex.quartets.append(sorted(tuple(int(row_item) for row_item in row)))
                else:
                    raise RuntimeError(
                        'more than 4 dimensions simplex is not supported'
                    )
        except EOFError as err:
            pass

        return complex
