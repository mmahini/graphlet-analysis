from complex.templates import NUM_OF_MINIPLEXES
from complex.entities.miniplex import Miniplex
from complex.entities.simplicial_complex import SimplicialComplex
from complex.utils.role import RoleUtils


class MiniplexStatistics():

    def __init__(self, complex: SimplicialComplex):
        self.complex = SimplicialComplex

        self.total_num_of_miniplexes = 0

        self.miniplex_cnt = [0 for _ in range(NUM_OF_MINIPLEXES)]
        self.miniplex_freq = [0.0 for _ in range(NUM_OF_MINIPLEXES)]
        
        self.miniplexes: dict[int, set] = dict()
        for n in range(NUM_OF_MINIPLEXES):
            self.miniplexes[n] = set()

        self.vertices_role: dict[int, dict] = dict()
        for v in complex.vertices:
            self.vertices_role[v] = RoleUtils().create_for_vertices()
            
        self.edges_role: dict[tuple, dict] = dict()
        for v in complex.vertices:
            for n in complex.nei[v]:
                if v < n:
                    self.edges_role[tuple([v,n])] = RoleUtils().create_for_vertices()
            
        self.triplets_role: dict[tuple, dict] = dict()
        for t in complex.triplets:
            self.triplets_role[tuple(t)] = RoleUtils().create_for_triplets()

    def add_statistic(self, miniplex: Miniplex, miniplex_type=-1, allow_duplicate=False):
        if miniplex_type == -1:
            miniplex_type = miniplex.get_type()

        duplicate = False
        if not allow_duplicate:
            if miniplex in self.miniplexes[miniplex_type]:
                duplicate = True

        if not duplicate:
            self.miniplexes[miniplex_type].add(miniplex)
            self.miniplex_cnt[miniplex_type] += 1
            self.total_num_of_miniplexes += 1
        
        self.calc_vertex_role(miniplex, miniplex_type)

    def calculate_frequencies(self):
        for i in range(NUM_OF_MINIPLEXES):
            self.miniplex_freq[i] = self.miniplex_cnt[i] / \
                self.total_num_of_miniplexes

    def calc_vertex_role(self, miniplex: Miniplex, miniplex_type=-1):
        for v in miniplex.vertices:
            if miniplex_type == 0:
                self.vertices_role[v][1] += 0.5
            elif miniplex_type == 1:
                if len(miniplex.nei[v]) > 1:
                    self.vertices_role[v][3] += 1
                else:
                    self.vertices_role[v][4] += 1
            elif miniplex_type in (2, 3):
                if len(miniplex.triplets) > 0:
                    self.vertices_role[v][8] += 1
                else:
                    self.vertices_role[v][6] += 1
            elif miniplex_type == 4:
                if len(miniplex.nei[v]) > 1:
                    self.vertices_role[v][11] += 1
                else:
                    self.vertices_role[v][12] += 1
            elif miniplex_type in (5, 6):
                if len(miniplex.nei[v]) == 1:
                    if len(miniplex.triplets) > 0:
                        self.vertices_role[v][23] += 1
                    else:
                        self.vertices_role[v][17] += 1
                elif len(miniplex.nei[v]) == 2:
                    if len(miniplex.triplets) > 0:
                        self.vertices_role[v][21] += 1
                    else:
                        self.vertices_role[v][15] += 1
                else:
                    if len(miniplex.triplets) > 0:
                        self.vertices_role[v][22] += 1
                    else:
                        self.vertices_role[v][16] += 1
            elif miniplex_type in (7,8,9):
                if len(miniplex.nei[v]) == 2:
                    if len(miniplex.triplets) == 0:
                        self.vertices_role[v][28] += 1
                    elif len(miniplex.triplets) == 1:
                        if v in miniplex.triplets[0]:
                            self.vertices_role[v][32] += 1
                        else:
                            self.vertices_role[v][34] += 1
                    else:
                        self.vertices_role[v][39] += 1
                else:
                    if len(miniplex.triplets) == 0:
                        self.vertices_role[v][29] += 1
                    elif len(miniplex.triplets) == 1:
                        self.vertices_role[v][33] += 1
                    else:
                        self.vertices_role[v][40] += 1
            elif miniplex_type == 10:
                if len(miniplex.nei[v]) > 1:
                    self.vertices_role[v][44] += 1
                else:
                    self.vertices_role[v][45] += 1
            elif miniplex_type == 11:
                self.vertices_role[v][47] += 1
            elif miniplex_type in (12, 13, 14, 15, 16, 17):
                if len(miniplex.quartets) == 1:
                    self.vertices_role[v][70] += 1
                elif len(miniplex.triplets) == 1:
                    if v in miniplex.triplets[0]:
                        self.vertices_role[v][51] += 1
                    else:
                        self.vertices_role[v][52] += 1
                elif len(miniplex.triplets) == 2:
                    if v in miniplex.triplets[0] and v in miniplex.triplets[1]:
                        self.vertices_role[v][57] += 1
                    else:
                        self.vertices_role[v][56] += 1
                elif len(miniplex.triplets) == 3:
                    if v in miniplex.triplets[0] and v in miniplex.triplets[1] and v in miniplex.triplets[2]:
                        self.vertices_role[v][63] += 1
                    else:
                        self.vertices_role[v][62] += 1
                elif len(miniplex.triplets) == 4:
                    self.vertices_role[v][67] += 1

    def write_frequencies(self):
        print("Miniplex Frequencies:")
        for i in range(NUM_OF_MINIPLEXES):
            print(f"{i}: {self.miniplex_freq[i]}")
            
    def write_roles(self):
        print("vertices role:")
        for v in range(len(self.vertices_role)):
            d = dict()
            for k in self.vertices_role[v]:
                if self.vertices_role[v][k] != 0:
                    d[k] = self.vertices_role[v][k]
            print(f"{v}: {d}")
        
        print("edges role:")
        for (k,v) in self.edges_role.items():
            d = dict()
            for (k2, v2) in v.items():
                if v2 != 0:
                    d[k] = self.edges_role[k][k2]
            print(f"{k}: {d}")
        
        print("triplets role:")
        for (k,v) in self.triplets_role.items():
            d = dict()
            for (k2, v2) in v.items():
                if v2 != 0:
                    d[k] = self.triplets_role[k][k2]
            print(f"{k}: {d}")

    def write(self):
        print(f"Miniplex Counts (total: {self.total_num_of_miniplexes}):")
        for i in range(NUM_OF_MINIPLEXES):
            print(f"{i}: {self.miniplex_cnt[i]}")
