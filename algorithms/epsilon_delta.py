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
