# Exact Graphlet count

from typing import List
from graph.graph import Graph
from graph.statistics import GraphletStatistics
from graph.graphlet import SubGraphletFactory
from algorithms.gfd import GfdAglorithm


class Exact(GfdAglorithm):

    # find exact number of graphlets with 2 vertices
    def gc0(self) -> None:
        for v in self.g.vertices:
            for u in self.g.nei[v]:
                sub_graphlet = SubGraphletFactory(
                ).create_subgraphlet(self.g, [v, u])
                self.gs.add_to_statistics(sub_graphlet, 0)

    # find exact number of graphlets with 3 vertices
    def gc3(self) -> None:
        for v in self.g.vertices:
            for u in self.g.nei[v]:
                for w in self.g.nei[v]:
                    if w == u:
                        continue

                    if w in self.g.nei[u]:
                        if w > u and u > v:
                            sub_graphlet = SubGraphletFactory(
                            ).create_subgraphlet(self.g, [v, u, w])
                            self.gs.add_to_statistics(sub_graphlet, 2)
                    else:
                        if w > u:
                            sub_graphlet = SubGraphletFactory(
                            ).create_subgraphlet(self.g, [v, u, w])
                            self.gs.add_to_statistics(sub_graphlet, 1)

    # find exact number of graphlets with 4 vertices
    def gc4(self) -> None:
        g = self.g
        gs = self.gs

        for v in g.vertices:
            for u in g.nei[v]:
                for w in g.nei[v]:
                    if w <= u:
                        continue

                    for x in g.nei[v]:
                        if x <= w:
                            continue
                        if w not in g.nei[u] and w not in g.nei[x] and u not in g.nei[x]:
                            sub_graphlet = SubGraphletFactory(
                            ).create_subgraphlet(g, [v, u, w, x])
                            self.gs.add_to_statistics(sub_graphlet, 4)

        for v in g.vertices:
            for u in g.nei[v]:
                for w in g.nei[u]:
                    if w == v:
                        continue
                    for x in g.nei[w]:
                        if x == v or x == u:
                            continue

                        sub_graphlet = SubGraphletFactory(
                        ).create_subgraphlet(g, [v, u, w, x])
                        e = sub_graphlet.countE()

                        if e == 6:
                            self.gs.add_to_statistics(sub_graphlet, 8)
                        elif e == 5:
                            self.gs.add_to_statistics(sub_graphlet, 7)
                        elif e == 3:
                            self.gs.add_to_statistics(sub_graphlet, 3)
                        # e = 4
                        elif v in g.nei[x]:
                            self.gs.add_to_statistics(sub_graphlet, 6)
                        # e = 4
                        elif u in g.nei[x]:
                            self.gs.add_to_statistics(sub_graphlet, 5)

    # find exact number of graphlets with 5 vertices
    def gc5(self) -> None:
        g = self.g
        gs = self.gs

        for v in g.vertices:
            for u in g.nei[v]:
                for w in g.nei[v]:
                    if w <= u:
                        continue
                    for x in g.nei[v]:
                        if x <= w:
                            continue
                        for y in g.nei[v]:
                            if y <= x:
                                continue

                            e: int = g.subgraph_countE([v, u, w, x, y])
                            sub_graphlet = SubGraphletFactory(
                            ).create_subgraphlet(g, [v, u, w, x, y])
                            deg: List = list()
                            for _ in range(5):
                                deg.append(0)
                            for i in {u, w, x, y}:
                                deg[g.subgraph_degree(i, [v, u, w, x, y])] += 1

                            if e == 4:
                                self.gs.add_to_statistics(sub_graphlet, 23)
                            elif e == 5:
                                self.gs.add_to_statistics(sub_graphlet, 19)
                            elif e == 6:
                                if deg[1] == 1 and deg[2] == 2 and deg[3] == 1:
                                    self.gs.add_to_statistics(sub_graphlet, 13)
                                if deg[2] == 4:
                                    self.gs.add_to_statistics(sub_graphlet, 20)
                            elif e == 7:
                                if deg[4] == 1 and deg[2] == 3:
                                    self.gs.add_to_statistics(sub_graphlet, 15)
                                if deg[3] == 3 and deg[1] == 1:
                                    self.gs.add_to_statistics(sub_graphlet, 18)
                                if deg[3] == 2 and deg[2] == 2:
                                    self.gs.add_to_statistics(sub_graphlet, 28)
                            elif e == 8:
                                if deg[3] == 4:
                                    self.gs.add_to_statistics(sub_graphlet, 22)
                                if deg[3] == 2 and deg[2] == 1:
                                    self.gs.add_to_statistics(sub_graphlet, 16)
                            elif e == 9:
                                self.gs.add_to_statistics(sub_graphlet, 17)
                            elif e == 10:
                                self.gs.add_to_statistics(sub_graphlet, 29)

        for v in g.vertices:
            for u in g.nei[v]:
                for w in g.nei[u]:
                    if w == v:
                        continue
                    for x in g.nei[w]:
                        if x == v or x == u:
                            continue
                        for y in g.nei[x]:
                            if y == v or y == u or y == w:
                                continue

                            e: int = g.subgraph_countE([v, u, w, x, y])
                            sub_graphlet = SubGraphletFactory(
                            ).create_subgraphlet(g, [v, u, w, x, y])
                            deg: List = list()
                            for _ in range(5):
                                deg.append(0)
                            for i in {v, u, w, x, y}:
                                deg[g.subgraph_degree(i, [v, u, w, x, y])] += 1

                            if e == 4:
                                self.gs.add_to_statistics(sub_graphlet, 9)
                            elif e == 5:
                                if deg[2] == 5:
                                    self.gs.add_to_statistics(sub_graphlet, 25)
                                if deg[2] == 1 and deg[3] == 2:
                                    self.gs.add_to_statistics(sub_graphlet, 26)
                                if deg[2] == 3 and deg[3] == 1 and w in g.nei[y]:
                                    self.gs.add_to_statistics(sub_graphlet, 11)
                                if deg[2] == 3 and deg[3] == 1 and u in g.nei[y]:
                                    self.gs.add_to_statistics(sub_graphlet, 12)
                            elif e == 6:
                                if deg[1] == 1 and deg[2] == 1 and deg[3] == 3:
                                    self.gs.add_to_statistics(sub_graphlet, 14)
                                if deg[2] == 3 and deg[3] == 2 and g.subgraph_countE([v, w, y]) == 0:
                                    self.gs.add_to_statistics(sub_graphlet, 24)
                                if deg[2] == 3 and deg[3] == 2 and y in g.nei[v]:
                                    self.gs.add_to_statistics(sub_graphlet, 27)
                            elif e == 7:
                                if deg[2] == 1 and deg[3] == 4:
                                    self.gs.add_to_statistics(sub_graphlet, 21)

        for v in g.vertices:
            for u in g.nei[v]:
                for w in g.nei[u]:
                    if w == v:
                        continue
                    for x in g.nei[w]:
                        if x == u or x == v:
                            continue
                        for y in g.nei[w]:
                            if y == u or y == v or y == x:
                                continue

                            e: int = g.subgraph_countE([v, u, w, x, y])
                            sub_graphlet = SubGraphletFactory(
                            ).create_subgraphlet(g, [v, u, w, x, y])
                            if e == 4:
                                self.gs.add_to_statistics(sub_graphlet, 10)

    # find exact number of graphlets with 2-5 vertices numbered (0-29)
    def run(self):
        if self.log:
            print("-------- extact --------")

        self.gc0()
        self.gc3()
        self.gc4()
        self.gc5()

        if self.log:
            self.gs.write()

        self.gs.calculate_frequencies()
        self.gs.calculate_gdc()
