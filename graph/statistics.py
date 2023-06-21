from typing import List

from graph.graph import Graph
from graph.graphlet import SubGraphlet, SubGraphletFactory, NUM_OF_GRAPHLETS, NUM_OF_ORBITS
from graph.templates import GraphletTemplates, OrbitTemplates


class GraphletStatistics():
    def __init__(self, g: Graph):
        self.g = g

        self.total_num_of_graphlets = 0
        self.total_num_of_orbits = 0

        self.graphlet_cnt = [0 for _ in range(NUM_OF_GRAPHLETS)]
        self.graphlet_freq = [0.0 for _ in range(NUM_OF_GRAPHLETS)]

        self.vertex_graphlet_cnt: dict[int, list] = dict()
        self.vertex_graphlet_freq: dict[int, list] = dict()
        for v in g.vertices:
            self.vertex_graphlet_cnt[v] = [0 for _ in range(NUM_OF_GRAPHLETS)]
            self.vertex_graphlet_freq[v] = [
                0.0 for _ in range(NUM_OF_GRAPHLETS)]

        self.vertex_orbit_cnt: dict[int, list] = dict()
        self.vertex_orbit_freq: dict[int, list] = dict()
        for v in g.vertices:
            self.vertex_orbit_cnt[v] = [0 for _ in range(NUM_OF_ORBITS)]
            self.vertex_orbit_freq[v] = [0.0 for _ in range(NUM_OF_ORBITS)]

    ################################
    def add_to_statistics(self, graphlet: SubGraphlet, graphlet_type=-1):
        if graphlet_type == -1:
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

    # remove duplicate counted graphlet that calculated during exact graphlet count calculation
    def down_scale_count(self, graphlet_type: int, coef: int):
        new_count = self.graphlet_cnt[graphlet_type] / coef
        self.total_num_of_graphlets -= (
            self.graphlet_cnt[graphlet_type] - new_count)
        self.graphlet_cnt[graphlet_type] = new_count

        for v in self.g.vertices:
            self.vertex_graphlet_cnt[v][graphlet_type] = self.vertex_graphlet_cnt[v][graphlet_type] / coef

            for (orbit_type, _) in OrbitTemplates().list()[graphlet_type]:
                self.vertex_orbit_cnt[v][orbit_type] = self.vertex_orbit_cnt[v][orbit_type] / coef

    ################################
    def write(self):
        print(f"Graphlet Counts (total: {self.total_num_of_graphlets}):")
        for i in range(NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_cnt[i]}")

        print("\n")
        print(f"Vertex Graphlet Counts:")
        for v in self.vertex_graphlet_cnt.keys():
            vertext_graphlet_count_dict = dict()
            for i in range(NUM_OF_GRAPHLETS):
                if self.vertex_graphlet_cnt[v][i] > 0:
                    vertext_graphlet_count_dict[i] = self.vertex_graphlet_cnt[v][i]
            print(f"{v}: {vertext_graphlet_count_dict}")

        print("\n")
        print(f"Vertex Orbit Counts:")
        for v in self.vertex_orbit_cnt.keys():
            vertext_orbit_count_dict = dict()
            for i in range(NUM_OF_ORBITS):
                if self.vertex_orbit_cnt[v][i] > 0:
                    vertext_orbit_count_dict[i] = self.vertex_orbit_cnt[v][i]
            print(f"{v}: {vertext_orbit_count_dict}")

    ################################
    def get_orbit_count(self):
        if self.total_num_of_orbits == 0:
            for v in self.vertex_orbit_cnt.keys():
                for i in range(NUM_OF_ORBITS):
                    self.total_num_of_orbits += self.vertex_orbit_cnt[v][i]

        return self.total_num_of_orbits

    ################################
    def calculate_frequencies(self):
        for i in range(NUM_OF_GRAPHLETS):
            self.graphlet_freq[i] = self.graphlet_cnt[i] / \
                self.total_num_of_graphlets

        for v in self.vertex_graphlet_freq.keys():
            for i in range(NUM_OF_GRAPHLETS):
                self.vertex_graphlet_freq[v][i] = self.vertex_graphlet_cnt[v][i] / \
                    self.total_num_of_graphlets

        # call to ensure obit count was generated
        self.get_orbit_count()
        
        for v in self.vertex_orbit_freq.keys():
            for i in range(NUM_OF_ORBITS):
                self.vertex_orbit_freq[v][i] = self.vertex_orbit_cnt[v][i] / \
                    self.total_num_of_orbits

    ################################
    def write_frequencies(self):
        print("Graphlet Frequencies:")
        for i in range(NUM_OF_GRAPHLETS):
            print(f"{i}: {self.graphlet_freq[i]}")

        print("\n")
        print(f"Vertex Graphlet Frequencies:")
        for v in self.vertex_graphlet_freq.keys():
            vertext_graphlet_freq_dict = dict()
            for i in range(NUM_OF_GRAPHLETS):
                if self.vertex_graphlet_freq[v][i] > 0:
                    vertext_graphlet_freq_dict[i] = self.vertex_graphlet_freq[v][i]
            print(f"{v}: {vertext_graphlet_freq_dict}")

        print("\n")
        print(f"Vertex Orbit Frequencies:")
        for v in self.vertex_orbit_freq.keys():
            vertext_orbit_freq_dict = dict()
            for i in range(NUM_OF_ORBITS):
                if self.vertex_orbit_freq[v][i] > 0:
                    vertext_orbit_freq_dict[i] = self.vertex_orbit_freq[v][i]
            print(f"{v}: {vertext_orbit_freq_dict}")