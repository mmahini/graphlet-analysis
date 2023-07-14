from utils.singleton import singleton


@singleton
class MfdUtils():

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
