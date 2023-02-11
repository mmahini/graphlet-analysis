from typing import List

from entities.graphlet import NUM_OF_GRAPHLETS

from entities.graph import Graph


class GraphletStatistics():
    def __init__(self, g: Graph):
        self.total_num_of_graphlets = 0

        self.graphlet_cnt: List = list()
        for _ in range(0, NUM_OF_GRAPHLETS):
            self.graphlet_cnt.append(0)
        self.graphlet_cnt[0] = g.e       # G0 : pair of connected vertices

        self.graphlet_freq: List = list()
        for _ in range(0, NUM_OF_GRAPHLETS):
            self.graphlet_freq.append(0.0)

    def plus_one(self, x: int):
        self.graphlet_cnt[x] = self.graphlet_cnt[x] + 1
        self.total_num_of_graphlets += 1

    def write(self):
        print(f"Graphlet Counts (total: {self.total_num_of_graphlets}):")
        for i in range(0, NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_cnt[i]}")

    def calculate_frequencies(self):
        for i in range(0, NUM_OF_GRAPHLETS):
            self.graphlet_freq[i] = self.graphlet_cnt[i] / \
                self.total_num_of_graphlets

    def write_frequencies(self):
        print("Graphlet Frequencies:")
        for i in range(0, NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_freq[i]}")
