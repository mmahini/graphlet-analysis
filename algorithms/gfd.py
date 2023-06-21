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
