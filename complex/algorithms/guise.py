from complex.statistics import MiniplexStatistics
from complex.core.miniplex_factory import MiniplexFactory
from complex.entities.miniplex import Miniplex
from complex.entities.simplicial_complex import SimplicialComplex
from complex.algorithms.mfd import MfdAglorithm
from random import randint, random


class Guise(MfdAglorithm):

    def populate_neighbor(self, miniplex: Miniplex) -> list[Miniplex]:
        neighbor_vertices = miniplex.get_neighbor_vertices()
        neighbors: list[Miniplex] = []

        # miniplex - {i}
        if len(miniplex.vertices) > 2:
            for i in miniplex.vertices:
                mp: Miniplex = MiniplexFactory().create_copy(miniplex)
                mp.remove_vertex(i)
                if mp.is_connected():
                    neighbors.append(mp)

        # miniplex - {i} + {v}
        for i in miniplex.vertices:
            for v in neighbor_vertices:
                mp: Miniplex = MiniplexFactory().create_copy(miniplex)
                mp.remove_vertex(i)
                mp.add_vertex(v)
                mp.add_vertex_simplex(v)
                if mp.is_connected():
                    neighbors.append(mp)

        if len(miniplex.vertices) < 4:
            # miniplex + {v}
            for v in neighbor_vertices:
                mp: Miniplex = MiniplexFactory().create_copy(miniplex)
                mp.add_vertex(v)
                # mp.add_vertex_simplex(v)
                if mp.is_connected():
                    neighbors.append(mp)

        return neighbors

    def get_initial_miniplex(self) -> Miniplex:
        miniplex: Miniplex = MiniplexFactory().create_instance(self.complex)

        v = -1
        for i in self.complex.vertices:
            if len(self.complex.nei[i]) >= 2:
                v = i
                break

        if v == -1:
            raise ValueError('wrong calculation of initial miniplex')

        miniplex.add_vertex(v)

        nei = list(self.complex.nei[v])
        miniplex.add_vertex(nei[0])
        miniplex.add_vertex(nei[1])

        miniplex.add_triplets()
        miniplex.add_quartets()

        return miniplex

    def random_walk(self, miniplex: Miniplex, steps: int, counting: bool):
        if (self.log):
            print("random walk started ...")

        neighbors: list[Miniplex] = self.populate_neighbor(miniplex)
        for i in range(steps):
            # random select from neighbors
            index = randint(0, len(neighbors)-1)
            selected_neighbor = neighbors[index]
            neighbors_of_neighbor = self.populate_neighbor(selected_neighbor)
            acceptance_probability = min(
                len(neighbors)/len(neighbors_of_neighbor), 1
            )
            if random() <= acceptance_probability:
                miniplex = selected_neighbor
                neighbors = neighbors_of_neighbor

            if counting:
                self.statistics.add_statistic(miniplex, allow_duplicate=True)

        return miniplex

    def run(self, stationary_steps: int, steps: int):
        if (self.log):
            print("-------- guise --------")

        random_miniplex: Miniplex = self.get_initial_miniplex()

        # get to stationary point
        if (self.log):
            print("guise :: start finding stationary ...")
        random_miniplex = self.random_walk(
            random_miniplex, stationary_steps, counting=False)

        # counting
        if (self.log):
            print("guise :: counting started ...")
        self.random_walk(random_miniplex, steps, counting=True)

        self.statistics.calculate_frequencies()
        if (self.log):
            self.statistics.write_frequencies()
