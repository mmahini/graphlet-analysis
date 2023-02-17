# Graphlet count

from typing import List
from entities.graph import Graph
from entities.graphlet_statistics import GraphletStatistics

# find exact number of graphlets with 3 vertices


def gc3(g: Graph, gs: GraphletStatistics) -> None:
    for v in g.vertices:
        for u in g.nei[v]:
            visited: set = {v, u}

            for w in g.nei[v]:
                if w in visited:
                    continue
                visited.add(w)

                if w in g.nei[u]:
                    if w > u and u > v:
                        gs.plus_one(2)
                else:
                    if w > u:
                        gs.plus_one(1)

# find exact number of graphlets with 4 vertices


def gc4(g: Graph, gs: GraphletStatistics) -> None:
    for v in g.vertices:
        for u in g.nei[v]:
            for w in g.nei[v]:
                if w <= u:
                    continue
                for x in g.nei[v]:
                    if x <= w:
                        continue
                    if w not in g.nei[u] and w not in g.nei[x] and u not in g.nei[x]:
                        gs.plus_one(4)

    for v in g.vertices:
        for u in g.nei[v]:
            for w in g.nei[u]:
                if w == v:
                    continue
                for x in g.nei[w]:
                    if x == u or x == v:
                        continue
                    e: int = g.subgraph_countE([v, u, w, x])
                    if e == 6:
                        gs.plus_one(8)
                    elif e == 5:
                        gs.plus_one(7)
                    elif e == 3:
                        gs.plus_one(3)
                    elif v in g.nei[x]:         # e = 4
                        gs.plus_one(6)
                    elif u in g.nei[x]:         # e = 4
                        gs.plus_one(5)

    gs.graphlet_cnt[3] = int(gs.graphlet_cnt[3]/2)
    gs.graphlet_cnt[5] = int(gs.graphlet_cnt[5]/2)
    gs.graphlet_cnt[6] = int(gs.graphlet_cnt[6]/8)
    gs.graphlet_cnt[7] = int(gs.graphlet_cnt[7]/12)
    gs.graphlet_cnt[8] = int(gs.graphlet_cnt[8]/24)


# find exact number of graphlets with 5 vertices
def gc5(g: Graph, gs: GraphletStatistics) -> None:
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
                        deg: List = list()
                        for _ in range(0, 5):
                            deg.append(0)
                        for i in {u, w, x, y}:
                            deg[g.subgraph_degree(i, [v, u, w, x, y])] += 1

                        if e == 4:
                            gs.plus_one(23)
                        elif e == 5:
                            gs.plus_one(19)
                        elif e == 6:
                            if deg[1] == 1 and deg[2] == 2 and deg[3] == 1:
                                gs.plus_one(13)
                            if deg[2] == 4:
                                gs.plus_one(20)
                        elif e == 7:
                            if deg[4] == 1 and deg[2] == 3:
                                gs.plus_one(15)
                            if deg[3] == 3 and deg[1] == 1:
                                gs.plus_one(18)
                            if deg[3] == 2 and deg[2] == 2:
                                gs.plus_one(28)
                        elif e == 8:
                            if deg[3] == 4:
                                gs.plus_one(22)
                            if deg[3] == 2 and deg[2] == 1:
                                gs.plus_one(16)
                        elif e == 9:
                            gs.plus_one(17)
                        elif e == 10:
                            gs.plus_one(29)

    for v in g.vertices:
        for u in g.nei[v]:
            for w in g.nei[u]:
                if w == v:
                    continue
                for x in g.nei[w]:
                    if x == u or x == v:
                        continue
                    for y in g.nei[x]:
                        if y == u or y == v or y == w:
                            continue
                        e: int = g.subgraph_countE([v, u, w, x, y])
                        deg: List = list()
                        for _ in range(0, 5):
                            deg.append(0)
                        for i in {v, u, w, x, y}:
                            deg[g.subgraph_degree(i, [v, u, w, x, y])] += 1

                        if e == 4:
                            gs.plus_one(9)
                        elif e == 5:
                            if deg[2] == 5:
                                gs.plus_one(25)
                            if deg[2] == 1 and deg[3] == 2:
                                gs.plus_one(26)
                            if deg[2] == 3 and deg[3] == 1 and w in g.nei[y]:
                                gs.plus_one(11)
                            if deg[2] == 3 and deg[3] == 1 and u in g.nei[y]:
                                gs.plus_one(12)
                        elif e == 6:
                            if deg[1] == 1 and deg[2] == 1 and deg[3] == 3:
                                gs.plus_one(14)
                            if deg[2] == 3 and deg[3] == 2 and y not in g.nei[v]:
                                gs.plus_one(24)
                            if deg[2] == 3 and deg[3] == 2 and y in g.nei[v]:
                                gs.plus_one(27)
                        elif e == 7:
                            gs.plus_one(21)

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
                        if e == 4:
                            gs.plus_one(10)

    gs.graphlet_cnt[9] = int(gs.graphlet_cnt[9]/2)
    gs.graphlet_cnt[14] = int(gs.graphlet_cnt[14]/8)
    gs.graphlet_cnt[10] = int(gs.graphlet_cnt[10]/2)
    gs.graphlet_cnt[15] = int(gs.graphlet_cnt[15]/2)
    gs.graphlet_cnt[16] = int(gs.graphlet_cnt[16]/2)
    gs.graphlet_cnt[17] = int(gs.graphlet_cnt[17]/3)
    gs.graphlet_cnt[24] = int(gs.graphlet_cnt[24]/12)
    gs.graphlet_cnt[25] = int(gs.graphlet_cnt[25]/10)
    gs.graphlet_cnt[27] = int(gs.graphlet_cnt[27]/10)
    gs.graphlet_cnt[29] = int(gs.graphlet_cnt[29]/5)

# find exact number of graphlets with 2-5 vertices numbered (0-29)


def exact_graphlet_count(g: Graph) -> None:
    gs: GraphletStatistics = GraphletStatistics(g)

    gc3(g, gs)
    gc4(g, gs)
    gc5(g, gs)

    gs.write()
