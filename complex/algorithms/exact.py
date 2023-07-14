# Exact Miniplex count

from complex.algorithms.mfd import MfdAglorithm
from complex.core.miniplex_factory import MiniplexFactory


class Exact(MfdAglorithm):

    # find exact number of miniplexes with 2 vertices
    def gc2(self) -> None:
        for v in self.complex.vertices:
            for u in self.complex.nei[v]:
                miniplex = MiniplexFactory().create_miniplex(
                    self.complex, [v, u])
                self.statistics.add_statistic(miniplex, 0)

        self.statistics.down_scale_count(miniplex_type=0, coef=2)

    # find exact number of miniplexes with 3 vertices
    def gc3(self) -> None:
        for v in self.complex.vertices:
            for u in self.complex.nei[v]:
                visited: set = {v, u}

                for w in self.complex.nei[v]:
                    if w in visited:
                        continue
                    visited.add(w)

                    if w in self.complex.nei[u]:
                        if w > u and u > v:
                            miniplex = MiniplexFactory().create_miniplex(
                                self.complex, [v, u, w]
                            )
                            if len(miniplex.triplets) > 0:
                                self.statistics.add_statistic(miniplex, 3)
                            else:
                                self.statistics.add_statistic(miniplex, 2)
                    else:
                        if w > u:
                            miniplex = MiniplexFactory().create_miniplex(
                                self.complex, [v, u, w]
                            )
                            self.statistics.add_statistic(miniplex, 1)

    # find exact number of miniplexes with 4 vertices
    def gc4(self) -> None:
        for v in self.complex.vertices:
            for u in self.complex.nei[v]:
                for w in self.complex.nei[v]:
                    if w <= u:
                        continue

                    for x in self.complex.nei[v]:
                        if x <= w:
                            continue
                        if w not in self.complex.nei[u] and w not in self.complex.nei[x] and u not in self.complex.nei[x]:
                            miniplex = MiniplexFactory().create_miniplex(
                                self.complex, [v, u, w, x]
                            )
                            self.statistics.add_statistic(miniplex, 10)

        for v in self.complex.vertices:
            for u in self.complex.nei[v]:
                for w in self.complex.nei[u]:
                    if w == v:
                        continue

                    for x in self.complex.nei[w]:
                        if x == u or x == v:
                            continue
                        miniplex = MiniplexFactory().create_miniplex(
                            self.complex, [v, u, w, x]
                        )
                        e = miniplex.countE()

                        if e == 6:
                            if len(miniplex.triplets) > 3:
                                if len(miniplex.quartets) > 0:
                                    self.statistics.add_statistic(miniplex, 20)
                                else:
                                    self.statistics.add_statistic(miniplex, 16)
                            elif len(miniplex.triplets) > 2:
                                if len(miniplex.quartets) > 0:
                                    self.statistics.add_statistic(miniplex, 19)
                                else:
                                    self.statistics.add_statistic(miniplex, 15)
                            elif len(miniplex.triplets) > 1:
                                if len(miniplex.quartets) > 0:
                                    self.statistics.add_statistic(miniplex, 18)
                                else:
                                    self.statistics.add_statistic(miniplex, 14)
                            elif len(miniplex.triplets) > 0:
                                if len(miniplex.quartets) > 0:
                                    self.statistics.add_statistic(miniplex, 17)
                                else:
                                    self.statistics.add_statistic(miniplex, 13)
                            else:
                                self.statistics.add_statistic(miniplex, 12)
                        elif e == 5:
                            if len(miniplex.triplets) > 1:
                                self.statistics.add_statistic(miniplex, 9)
                            elif len(miniplex.triplets) > 0:
                                self.statistics.add_statistic(miniplex, 8)
                            else:
                                self.statistics.add_statistic(miniplex, 7)
                        elif e == 3:
                            self.statistics.add_statistic(miniplex, 4)
                        # e = 4
                        elif v in g.nei[x]:
                            self.statistics.add_statistic(miniplex, 11)
                        # e = 4
                        elif u in g.nei[x]:
                            if len(miniplex.triplets) > 0:
                                self.statistics.add_statistic(miniplex, 6)
                            else:
                                self.statistics.add_statistic(miniplex, 5)

        # self.statistics.down_scale_count(miniplex_type=3, coef=2)
        # self.statistics.down_scale_count(miniplex_type=5, coef=2)
        # self.statistics.down_scale_count(miniplex_type=6, coef=8)
        # self.statistics.down_scale_count(miniplex_type=7, coef=12)
        # self.statistics.down_scale_count(miniplex_type=8, coef=24)

    # find exact number of miniplexes with 2-5 vertices numbered (0-29)
    def run(self):
        if self.log:
            print("running extact miniplex count")

        self.gc2()
        self.gc3()
        self.gc4()

        if self.log:
            self.statistics.write()

        self.statistics.calculate_frequencies()
