from typing import List

from entities.graphlet import NUM_OF_GRAPHLETS, NUM_OF_ORBITS
from entities.graph import Graph
from entities.graphlet import SubGraphlet, SubGraphletFactory
from entities.graphlet_templates import GraphletTemplates


class GraphletStatistics():
    def __init__(self, g: Graph):
        self.total_num_of_graphlets = 0

        self.graphlet_cnt = [0 for _ in range(0, NUM_OF_GRAPHLETS)]
        self.graphlet_freq = [0.0 for _ in range(0, NUM_OF_GRAPHLETS)]

        self.vertex_graphlet_cnt: dict[int, list] = dict()
        self.vertex_graphlet_freq: dict[int, list] = dict()
        for v in g.vertices:
            self.vertex_graphlet_cnt[v] = [0 for _ in range(0, NUM_OF_GRAPHLETS)]
            self.vertex_graphlet_freq[v] = [0.0 for _ in range(0, NUM_OF_GRAPHLETS)]

        self.vertex_orbit_cnt: dict[int, list] = dict()
        self.vertex_orbit_freq: dict[int, list] = dict()
        for v in g.vertices:
            self.vertex_orbit_cnt[v] = [0 for _ in range(0, NUM_OF_ORBITS)]
            self.vertex_orbit_freq[v] = [0.0 for _ in range(0, NUM_OF_ORBITS)]

    def add_to_statistics(self, graphlet: SubGraphlet):
        graphlet_type = graphlet.get_graphlet_type()
        # plus_one_graphlet
        self.graphlet_cnt[graphlet_type] += 1
        for v in graphlet.vertices:
            # plus_one_graphlet_to_vertex
            self.vertex_graphlet_cnt[v][graphlet_type] += 1
            # plus_one_orbit_to_vertex
            orbit_type = graphlet.get_orbit_type(v)
            self.vertex_orbit_cnt[v][orbit_type] += 1

        self.total_num_of_graphlets += 1

    # it would be good to change method name to add_statistics_by_type
    def plus_one(self, graphlet_type: int):
        graph_from_type = GraphletTemplates().list()[graphlet_type]
        to_add_graphlet = SubGraphletFactory().copy_from_graph(graph_from_type)
        self.add_to_statistics(to_add_graphlet)

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
                self.vertex_graphlet_freq[v][i] = self.vertex_graphlet_cnt[v][i] / \
                    self.total_num_of_graphlets

    def write_frequencies(self):
        print("Graphlet Frequencies:")
        for i in range(0, NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_freq[i]}")
