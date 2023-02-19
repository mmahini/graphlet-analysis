from entities.graph import Graph
from entities.graphlet_statistics import GraphletStatistics
from entities.graphlet import NUM_OF_GRAPHLETS
from abc import ABC

class GfdAglorithm(ABC):
    def __init__(self, g: Graph):
        self.g = g
        self.gs: GraphletStatistics = GraphletStatistics(g)
        self.log = False
    

class EpsilonDelta():
    def __init__(self):
        self.samples = 0
        self.epsilon = [0.1, 0.05, 0.02, 0.01]
        self.out_range = dict()
        self.delta = dict()
        for e in self.epsilon:
            self.out_range[e] = 0
            self.delta[e] = 0

    def calc_error(self, alg: GfdAglorithm,  exact: GfdAglorithm):
        error = list()
        for i in range(0, NUM_OF_GRAPHLETS):
            if exact.gs.graphlet_freq[i] == 0:
                error.append(-1)
            else:
                error.append(abs(alg.gs.graphlet_freq[i] - exact.gs.graphlet_freq[i]))
        return error

    def append_error(self, error: list):
        for i in range(0, NUM_OF_GRAPHLETS):
            if error[i] == -1:
                continue
            self.samples += 1
            for e in self.epsilon:
                if error[i] > e:
                    self.out_range[e] += 1

    def calc_delta(self):
        for e in self.epsilon:
            self.delta[e] = 1 - (self.out_range[e]/self.samples)

    def write(self):
        print(f"Delta Statistics for Every Epsilon (samples: {self.samples})")
        for e in self.epsilon:
            print(f"{e}: {self.delta[e]*100}")