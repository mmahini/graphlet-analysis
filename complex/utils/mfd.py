from utils.singleton import singleton
from complex.algorithms.mfd import MfdAglorithm
from complex.templates import NUM_OF_MINIPLEXES


@singleton
class MfdUtils():

    def calc_miniplex_count_error(self, guise: MfdAglorithm,  exact: MfdAglorithm):
        error = list()
        for i in range(NUM_OF_MINIPLEXES):
            if exact.statistics.miniplex_freq[i] == 0:
                error.append(-1)
            else:
                error.append(
                    abs(guise.statistics.miniplex_freq[i] -
                        exact.statistics.miniplex_freq[i])
                )
        return error

    def calc_vertices_role_error(self, guise: MfdAglorithm,  exact: MfdAglorithm):
        error: dict[int, float] = dict()

        for (k,v) in exact.statistics.vertices_role.items():
            total_err = 0
            for (k2, v2) in v.items():
                if v2 != 0:
                    total_err =+ abs((v2 / exact.statistics.total_num_of_miniplexes) - (guise.statistics.vertices_role[k][k2] / guise.statistics.total_num_of_miniplexes))
            
            error[k] = total_err / len(v.keys())
    
        return error

    def calc_edges_role_error(self, guise: MfdAglorithm,  exact: MfdAglorithm):
        error: dict[int, float] = dict()

        for (k,v) in exact.statistics.edges_role.items():
            total_err = 0
            for (k2, v2) in v.items():
                if v2 != 0:
                    total_err =+ abs((v2 / exact.statistics.total_num_of_miniplexes) - (guise.statistics.edges_role[k][k2] / guise.statistics.total_num_of_miniplexes))
            
            error[k] = total_err / len(v.keys())
    
        return error
    
    def calc_triplets_role_error(self, guise: MfdAglorithm,  exact: MfdAglorithm):
        error: dict[int, float] = dict()

        for (k,v) in exact.statistics.triplets_role.items():
            total_err = 0
            for (k2, v2) in v.items():
                if v2 != 0:
                    total_err =+ abs((v2 / exact.statistics.total_num_of_miniplexes) - (guise.statistics.triplets_role[k][k2] / guise.statistics.total_num_of_miniplexes))
            
            error[k] = total_err / len(v.keys())
    
        return error
