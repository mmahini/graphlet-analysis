from utils.singleton import singleton
from graph.graph import Graph
from graph.statistics import GraphletStatistics
from graph.graphlet import NUM_OF_GRAPHLETS, NUM_OF_ORBITS
from abc import ABC


class GfdAglorithm(ABC):
    def __init__(self, g: Graph):
        self.g = g
        self.gs: GraphletStatistics = GraphletStatistics(g)
        self.log = False


class EpsilonDelta():
    def __init__(self, epsilons: list):
        self.samples = 0
        self.epsilon = epsilons

        self.out_range = dict()
        self.delta = dict()
        for e in self.epsilon:
            self.out_range[e] = 0
            self.delta[e] = 0

    def append_graphlet_count_error(self, error: list):
        for i in range(len(error)):
            if error[i] == -1:
                continue

            self.samples += 1
            for e in self.epsilon:
                if error[i] > e:
                    self.out_range[e] += 1

    def append_vertex_count_error(self,  error: dict[int, list]):
        for k in error.keys():
            for l in error[k]:
                if l == -1:
                    continue

                self.samples += 1
                for e in self.epsilon:
                    if l > e:
                        self.out_range[e] += 1

    def append_vertex_graphlet_degree_centrality_error(self,  error: dict[int, float]):
        for k in error.keys():
            i = error[k]
            if i == -1:
                continue

            self.samples += 1
            for e in self.epsilon:
                if i > e:
                    self.out_range[e] += 1

    def calc_delta(self):
        for e in self.epsilon:
            self.delta[e] = 1 - (self.out_range[e]/self.samples)

    def write(self):
        print(f"Delta Statistics for Every Epsilon (samples: {self.samples})")
        for e in self.epsilon:
            print(f"{e}: {self.delta[e]*100}")


@singleton
class GfdUtils():

    def calc_graphlet_count_error(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        error = list()
        for i in range(NUM_OF_GRAPHLETS):
            if exact.gs.graphlet_freq[i] == 0:
                error.append(-1)
            else:
                error.append(
                    abs(alg.gs.graphlet_freq[i] - exact.gs.graphlet_freq[i]))
        return error

    def calc_vertex_graphlet_count_error(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        error: dict[int, list] = dict()

        for v in exact.gs.vertex_graphlet_freq.keys():
            error[v] = list()

            for i in range(NUM_OF_GRAPHLETS):
                if exact.gs.vertex_graphlet_freq[v][i] == 0:
                    error[v].append(-1)
                else:
                    error[v].append(abs(
                        alg.gs.vertex_graphlet_freq[v][i] - exact.gs.vertex_graphlet_freq[v][i]))

        return error

    def calc_vertex_orbit_count_error(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        error: dict[int, list] = dict()

        for v in exact.gs.vertex_orbit_freq.keys():
            error[v] = list()

            for i in range(NUM_OF_ORBITS):
                if exact.gs.vertex_orbit_freq[v][i] == 0:
                    error[v].append(-1)
                else:
                    error[v].append(abs(
                        alg.gs.vertex_orbit_freq[v][i] - exact.gs.vertex_orbit_freq[v][i]))

        return error

    def calc_vertex_graphlet_degree_centrality_error(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        error: dict[int, float] = dict()

        for v in exact.gs.vertex_gdc.keys():
            if exact.gs.vertex_gdc[v] == 0:
                error[v] = -1
            else:
                error[v] = abs(alg.gs.vertex_gdc[v] - exact.gs.vertex_gdc[v])

        return error

    def calc_gfd_top_kـcorrectness(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        top_k_correctness = list()
        for i in [1, 2, 4]:
            correctness = self.calc_top_kـcorrectness(
                dict(enumerate(alg.gs.graphlet_freq)),
                dict(enumerate(exact.gs.graphlet_freq)),
                i * 5)
            top_k_correctness.append(correctness)
        return top_k_correctness

    def calc_gcd_top_kـcorrectness(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        top_k_correctness = list()
        for i in [1, 2, 4]:
            correctness = self.calc_top_kـcorrectness(
                alg.gs.vertex_gdc,
                exact.gs.vertex_gdc,
                i * 5)
            top_k_correctness.append(correctness)
        return top_k_correctness

    def calc_top_kـcorrectness(self, d1: dict,  d2: dict, k: int):
        l1 = list(d1.items())
        l2 = list(d2.items())

        l1.sort(reverse=True, key=lambda x: x[1])
        l2.sort(reverse=True, key=lambda x: x[1])

    
        list_a = list(map(lambda x: x[0], l1[0: k])) # [i[0] for i in l1]
        list_b = list(map(lambda x: x[0], l2[0: k])) # [i[0] for i in l2]

        # Get the number of elements in list B that exist in list A
        common_elements = len(set(list_b).intersection(list_a))
        # Calculate the percentage of list B existing in list A
        percentage = (common_elements/len(list_b)) * 100

        return percentage
