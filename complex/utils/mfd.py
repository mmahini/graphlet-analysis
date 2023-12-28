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
