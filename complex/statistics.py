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
                    self.edges_role[tuple([v,n])] = RoleUtils().create_for_edges()
            
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
                self.vertices_role[v][1] += 1
                #
                for n in miniplex.nei[v]:
                    if v < n:
                        self.edges_role[tuple([v,n])][2] += 1
            elif miniplex_type == 1:
                if len(miniplex.nei[v]) > 1:
                    self.vertices_role[v][3] += 1
                else:
                    self.vertices_role[v][4] += 1
                #    
                for n in miniplex.nei[v]:
                    if v < n:
                        self.edges_role[tuple([v,n])][5] += 1
            elif miniplex_type in (2, 3):
                if len(miniplex.triplets) > 0:
                    self.vertices_role[v][8] += 1
                    #
                    for n in miniplex.nei[v]:
                        if v < n:
                            self.edges_role[tuple([v,n])][9] += 1
                    #
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][10] += 1
                else:
                    self.vertices_role[v][6] += 1
                    #
                    for n in miniplex.nei[v]:
                        if v < n:
                            self.edges_role[tuple([v,n])][7] += 1
            elif miniplex_type == 4:
                if len(miniplex.nei[v]) > 1:
                    self.vertices_role[v][11] += 1
                    #
                    for n in miniplex.nei[v]:
                        if v < n and len(miniplex.nei[n]) > 1:
                            self.edges_role[tuple(sorted([v,n]))][13] += 1
                else:
                    self.vertices_role[v][12] += 1
                    #
                    for n in miniplex.nei[v]:
                        self.edges_role[tuple(sorted([v,n]))][14] += 1
            elif miniplex_type in (5, 6):
                if len(miniplex.nei[v]) == 1:
                    if len(miniplex.triplets) > 0:
                        self.vertices_role[v][23] += 1
                    else:
                        self.vertices_role[v][17] += 1
                elif len(miniplex.nei[v]) == 2:
                    if len(miniplex.triplets) > 0:
                        self.vertices_role[v][21] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and len(miniplex.nei[n]) == 2:
                                self.edges_role[tuple([v,n])][24] += 1
                    else:
                        self.vertices_role[v][15] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and len(miniplex.nei[n]) == 2:
                                self.edges_role[tuple([v,n])][18] += 1
                else:
                    if len(miniplex.triplets) > 0:
                        self.vertices_role[v][22] += 1
                        #
                        for n in miniplex.nei[v]:
                            if len(miniplex.nei[n]) == 1:
                                self.edges_role[tuple(sorted([v,n]))][26] += 1
                            else:
                                self.edges_role[tuple(sorted([v,n]))][25] += 1
                    else:
                        self.vertices_role[v][16] += 1
                        #
                        for n in miniplex.nei[v]:
                            if len(miniplex.nei[n]) == 1:
                                self.edges_role[tuple(sorted([v,n]))][20] += 1
                            else:
                                self.edges_role[tuple(sorted([v,n]))][19] += 1
                #
                if len(miniplex.triplets) > 0:
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][27] += 1
            elif miniplex_type in (7,8,9):
                if len(miniplex.nei[v]) == 2:
                    if len(miniplex.triplets) == 0:
                        self.vertices_role[v][28] += 1
                        #
                        for n in miniplex.nei[v]:
                            self.edges_role[tuple(sorted([v,n]))][30] += 1
                    elif len(miniplex.triplets) == 1:
                        if v in miniplex.triplets[0]:
                            self.vertices_role[v][32] += 1
                            #
                            for n in miniplex.nei[v]:
                                self.edges_role[tuple(sorted([v,n]))][35] += 1
                        else:
                            self.vertices_role[v][34] += 1
                            #
                            for n in miniplex.nei[v]:
                                self.edges_role[tuple(sorted([v,n]))][37] += 1
                        #
                        for t in miniplex.triplets:
                           self.triplets_role[tuple(sorted(t))][38] += 1
                    else:
                        self.vertices_role[v][39] += 1
                        #
                        for n in miniplex.nei[v]:
                            self.edges_role[tuple(sorted([v,n]))][41] += 1
                        #
                        for t in miniplex.triplets:
                           self.triplets_role[tuple(sorted(t))][43] += 1
                else:
                    if len(miniplex.triplets) == 0:
                        self.vertices_role[v][29] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and len(miniplex.nei[n]) == 3:
                                self.edges_role[tuple([v,n])][31] += 1
                    elif len(miniplex.triplets) == 1:
                        self.vertices_role[v][33] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and len(miniplex.nei[n]) == 3:
                                self.edges_role[tuple([v,n])][36] += 1
                    else:
                        self.vertices_role[v][40] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and len(miniplex.nei[n]) == 3:
                                self.edges_role[tuple([v,n])][42] += 1
            elif miniplex_type == 10:
                if len(miniplex.nei[v]) > 1:
                    self.vertices_role[v][44] += 1
                else:
                    self.vertices_role[v][45] += 1
                #
                for n in miniplex.nei[v]:
                    if v < n:
                        self.edges_role[tuple([v,n])][46] += 1
            elif miniplex_type == 11:
                self.vertices_role[v][47] += 1
                #
                for n in miniplex.nei[v]:
                    if v < n:
                        self.edges_role[tuple([v,n])][48] += 1
            elif miniplex_type in (12, 13, 14, 15, 16, 17):
                if len(miniplex.quartets) == 1:
                    self.vertices_role[v][70] += 1
                    #
                    for n in miniplex.nei[v]:
                        if v < n:
                            self.edges_role[tuple([v,n])][71] += 1
                    #
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][72] += 1
                elif len(miniplex.triplets) == 0:
                    self.vertices_role[v][49] += 1
                    #
                    for n in miniplex.nei[v]:
                        if v < n:
                            self.edges_role[tuple([v,n])][50] += 1
                elif len(miniplex.triplets) == 1:
                    if v in miniplex.triplets[0]:
                        self.vertices_role[v][51] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and n in miniplex.triplets[0]:
                                self.edges_role[tuple([v,n])][53] += 1
                    else:
                        self.vertices_role[v][52] += 1
                        #
                        for n in miniplex.nei[v]:
                            self.edges_role[tuple(sorted([v,n]))][54] += 1
                    #
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][55] += 1
                elif len(miniplex.triplets) == 2:
                    if v in miniplex.triplets[0] and v in miniplex.triplets[1]:
                        self.vertices_role[v][57] += 1
                        #
                        for n in miniplex.nei[v]:
                            if n in miniplex.triplets[0] and n in miniplex.triplets[1]:
                                self.edges_role[tuple(sorted([v,n]))][59] += 1
                            else:
                                self.edges_role[tuple(sorted([v,n]))][58] += 1
                    else:
                        self.vertices_role[v][56] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n and n not in miniplex.triplets[0] and n not in miniplex.triplets[1]:
                                self.edges_role[tuple([v,n])][60] += 1
                    #
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][61] += 1
                elif len(miniplex.triplets) == 3:
                    if v in miniplex.triplets[0] and v in miniplex.triplets[1] and v in miniplex.triplets[2]:
                        self.vertices_role[v][63] += 1
                        #
                        for n in miniplex.nei[v]:
                            if v < n:
                                self.edges_role[tuple([v,n])][65] += 1
                            for n2 in miniplex.nei[v]:
                                if n < n2:
                                    self.edges_role[tuple([n,n2])][64 ] += 1
                    else:
                        self.vertices_role[v][62] += 1
                    #
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][66] += 1
                elif len(miniplex.triplets) == 4:
                    self.vertices_role[v][67] += 1
                    #
                    for n in miniplex.nei[v]:
                        if v < n:
                            self.edges_role[tuple([v,n])][68] += 1
                    #
                    for t in miniplex.triplets:
                        self.triplets_role[tuple(sorted(t))][69] += 1
            

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
                    d[k] = int(self.vertices_role[v][k] / RoleUtils().vertices_coefficient(k))
            print(f"{v}: {d}")
        
        print("edges role:")
        for (k,v) in self.edges_role.items():
            d = dict()
            for (k2, v2) in v.items():
                if v2 != 0:
                    d[k2] = int(self.edges_role[k][k2] / RoleUtils().edges_coefficient(k2))
            print(f"{k}: {d}")
        
        print("triplets role:")
        for (k,v) in self.triplets_role.items():
            d = dict()
            for (k2, v2) in v.items():
                if v2 != 0:
                    d[k2] = int(self.triplets_role[k][k2] / RoleUtils().triplets_coefficient(k2))
            print(f"{k}: {d}")

    def write(self):
        print(f"Miniplex Counts (total: {self.total_num_of_miniplexes}):")
        for i in range(NUM_OF_MINIPLEXES):
            print(f"{i}: {self.miniplex_cnt[i]}")
