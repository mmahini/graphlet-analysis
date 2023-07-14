from complex.templates import NUM_OF_MINIPLEXES
from complex.entities.miniplex import Miniplex
from complex.entities.simplicial_complex import SimplicialComplex


class MiniplexStatistics():

    def __init__(self, complex: SimplicialComplex):
        self.complex = SimplicialComplex

        self.total_num_of_miniplexes = 0

        self.miniplex_cnt = [0 for _ in range(NUM_OF_MINIPLEXES)]
        self.miniplex_freq = [0.0 for _ in range(NUM_OF_MINIPLEXES)]

    def add_statistic(self, miniplex: Miniplex, miniplex_type=-1):
        if miniplex_type == -1:
            miniplex_type = miniplex.get_type()

        self.miniplex_cnt[miniplex_type] += 1

        self.total_num_of_miniplexes += 1

    # remove duplicate counted miniplex that calculated during exact miniplex count calculation
    def down_scale_count(self, miniplex_type: int, coef: int):
        new_count = self.miniplex_cnt[miniplex_type] / coef
        self.total_num_of_miniplexes -= (
            self.miniplex_cnt[miniplex_type] - new_count)
        self.miniplex_cnt[miniplex_type] = int(new_count)

    def calculate_frequencies(self):
        for i in range(NUM_OF_MINIPLEXES):
            self.miniplex_freq[i] = self.miniplex_cnt[i] / \
                self.total_num_of_miniplexes

    def write_frequencies(self):
        print("Miniplex Frequencies:")
        for i in range(NUM_OF_MINIPLEXES):
            print(f"{i}: {self.miniplex_freq[i]}")

    def write(self):
        print(f"Miniplex Counts (total: {self.total_num_of_miniplexes}):")
        for i in range(NUM_OF_MINIPLEXES):
            print(f"{i}: {self.miniplex_cnt[i]}")
