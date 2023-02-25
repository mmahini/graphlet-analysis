from typing import List

from entities.graphlet import NUM_OF_GRAPHLETS

from entities.graph import Graph
from entities.graphlet import SubGraphlet


class GraphletStatistics():
    def __init__(self, g: Graph):
        self.total_num_of_graphlets = 0

        self.graphlet_cnt = [0 for _ in range(0, NUM_OF_GRAPHLETS)]
        self.graphlet_freq = [0.0 for _ in range(0, NUM_OF_GRAPHLETS)]

        self.vertex_graphlet_cnt: dict[int, list]
        self.vertex_graphlet_freq: dict[int, list]
        for v in g.vertices:
            self.vertex_graphlet_cnt[v] = [0 for _ in range(0, NUM_OF_GRAPHLETS)]
            self.vertex_graphlet_freq[v] = [0.0 for _ in range(0, NUM_OF_GRAPHLETS)]

    def plus_one(self, graphlet_type: int):
        self.graphlet_cnt[graphlet_type] += 1
        self.total_num_of_graphlets += 1

    def plus_one_to_vertex(self, vertex: int, graphlet_type: int):
        self.vertex_graphlet_cnt[vertex][graphlet_type] += 1

    def add_to_statistics(self, graphlet: SubGraphlet):
        graphlet_type = graphlet.get_graphlet_type()
        self.plus_one(graphlet_type)
        for v in graphlet.vertices:
            self.plus_one_to_vertex(v, graphlet_type)

    def write(self):
        print(f"Graphlet Counts (total: {self.total_num_of_graphlets}):")
        for i in range(0, NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_cnt[i]}")

    def calculate_frequencies(self):
        for i in range(0, NUM_OF_GRAPHLETS):
            self.graphlet_freq[i] = self.graphlet_cnt[i] / \
                self.total_num_of_graphlets

        for v in self.vertex_graphlet_freq.keys():
            for i in range(0, NUM_OF_GRAPHLETS):
                self.vertex_graphlet_freq[i] = self.vertex_graphlet_cnt[v][i] / \
                    self.total_num_of_graphlets


    def write_frequencies(self):
        print("Graphlet Frequencies:")
        for i in range(0, NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_freq[i]}")
