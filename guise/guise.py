from entities.graphlet import SubGraphlet, SubGraphletFactory, NUM_OF_GRAPHLETS
from entities.graphlet_statistics import GraphletStatistics
from entities.graph import Graph
from random import randint, random
from graph_algorithms.gfd_algorithm import GfdAglorithm


class Guise(GfdAglorithm):

    def populate_neighbor(self, sub_graphlet: SubGraphlet) -> list[SubGraphlet]:
        neighbor_vertices = sub_graphlet.get_neighbor_vertices()
        neighbors: list[SubGraphlet] = []

        # sub_graphlet - {i}
        if sub_graphlet.countV() > 2:
            for i in sub_graphlet.vertices:
                sg: SubGraphlet = SubGraphletFactory().get_copy(sub_graphlet)
                sg.remove(i)
                if sg.is_connected():
                    neighbors.append(sg)

        # sub_graphlet - {i} + {v}
        for i in sub_graphlet.vertices:
            for v in neighbor_vertices:
                sg: SubGraphlet = SubGraphletFactory().get_copy(sub_graphlet)
                sg.remove(i)
                sg.add(v)
                if sg.is_connected():
                    neighbors.append(sg)

        if sub_graphlet.countV() < 5:
            # sub_graphlet + {v}
            for v in neighbor_vertices:
                sg: SubGraphlet = SubGraphletFactory().get_copy(sub_graphlet)
                sg.add(v)
                if sg.is_connected():
                    neighbors.append(sg)

        return neighbors

    def get_initial_graphlet(self) -> SubGraphlet:
        sub_graphlet: SubGraphlet = SubGraphletFactory().get_instance(self.g)

        v = -1
        for i in self.g.vertices:
            if len(self.g.nei[i]) >= 2:
                v = i
                break

        if v == -1:
            if (self.log):
                print("Shiiiiiiiit !!!")

        sub_graphlet.add(v)

        nei = list(self.g.nei[v])
        sub_graphlet.add(nei[0])
        sub_graphlet.add(nei[1])

        return sub_graphlet

    def random_walk(self, sub_graph: SubGraphlet, steps: int, counting: bool):
        if (self.log):
            print("random walk started ...")
        neighbors: list[SubGraphlet] = self.populate_neighbor(sub_graph)
        for i in range(steps):
            # random select from neighbors
            index = randint(0, len(neighbors)-1)
            selected_neighbor = neighbors[index]
            neighbors_of_neighbor = self.populate_neighbor(selected_neighbor)
            acceptance_probability = min(
                len(neighbors)/len(neighbors_of_neighbor), 1)
            if random() <= acceptance_probability:
                sub_graph = selected_neighbor
                neighbors = neighbors_of_neighbor

            if counting:
                self.gs.add_to_statistics(sub_graph)

        return sub_graph

    def run(self, stationary_steps: int, steps: int):
        if (self.log):
            print("-------- guise --------")

        random_sub_graphlet: SubGraphlet = self.get_initial_graphlet()

        # get to stationary point
        if (self.log):
            print("guise :: start finding stationary ...")
        random_sub_graphlet = self.random_walk(
            random_sub_graphlet, stationary_steps, counting=False)

        # counting
        if (self.log):
            print("guise :: counting started ...")
        self.random_walk(random_sub_graphlet, steps, counting=True)

        self.gs.calculate_frequencies()
        if (self.log):
            self.gs.write_frequencies()
