# Graphlet count

from typing import List
from graph import Graph

# find exact number of graphlets with 3 vertices 
def gc3(g: Graph, graphlet_cnt: List) -> None:
    for v in range(0,g.n):
        for u in g.nei[v]:
            visited: set = {v, u}

            for w in g.nei[v]:
                if w in visited:
                    continue
                visited.add(w)

                if w in g.nei[u]:
                    if w > u and u > v:
                        graphlet_cnt[2] = graphlet_cnt[2] + 1
                else:
                    if w > u:
                        graphlet_cnt[1] = graphlet_cnt[1] + 1

# find exact number of graphlets with 4 vertices 
def gc4(g: Graph, graphlet_cnt: List) -> None:  
    for v in range(0,g.n):
        for u in g.nei[v]:
            for w in g.nei[v]:
                if w <= u:
                    continue
                for x in g.nei[v]:
                    if x <= w:
                        continue
                    if w not in g.nei[u] and w not in g.nei[x] and u not in g.nei[x]:
                        graphlet_cnt[4] = graphlet_cnt[4] + 1
            
    for v in range(0,g.n):
        for u in g.nei[v]:
            for w in g.nei[u]:
                if w == v:
                    continue
                for x in g.nei[w]:
                    if x == u or x == v:
                        continue
                    e: int = g.countE([v,u,w,x])
                    if e == 6:
                        graphlet_cnt[8] = graphlet_cnt[8] + 1
                    elif e == 5:
                        graphlet_cnt[7] = graphlet_cnt[7] + 1
                    elif e == 3:
                        graphlet_cnt[3] = graphlet_cnt[3] + 1
                    elif v in g.nei[x]:         # e = 4
                        graphlet_cnt[6] = graphlet_cnt[6] + 1
                    elif u in g.nei[x]:         # e = 4
                        graphlet_cnt[5] = graphlet_cnt[5] + 1
    
    graphlet_cnt[3] = int(graphlet_cnt[3]/2)
    graphlet_cnt[5] = int(graphlet_cnt[5]/2)
    graphlet_cnt[6] = int(graphlet_cnt[6]/8)
    graphlet_cnt[7] = int(graphlet_cnt[7]/12)
    graphlet_cnt[8] = int(graphlet_cnt[8]/24)


# find exact number of graphlets with 5 vertices 
def gc5(g: Graph, graphlet_cnt: List) -> None:
    for v in range(0,g.n):
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
                        e: int = g.countE([v,u,w,x,y])
                        deg: List = list()
                        for _ in range(0,5):
                            deg.append(0)
                        for i in {u,w,x,y}:                                
                            deg[g.degree(i, [v,u,w,x,y])] += 1

                        if e == 4:
                            graphlet_cnt[23] = graphlet_cnt[23] + 1
                        elif e == 5:
                            graphlet_cnt[19] = graphlet_cnt[19] + 1
                        elif e == 6:
                            if deg[1] == 1 and deg[2] == 2 and deg[3] == 1:                                
                                graphlet_cnt[13] = graphlet_cnt[13] + 1
                            if deg[2] == 4: 
                                graphlet_cnt[20] = graphlet_cnt[20] + 1
                        elif e == 7:
                            if deg[4] == 1 and deg[2] == 3:                                
                                graphlet_cnt[15] = graphlet_cnt[15] + 1
                            if deg[3] == 3 and deg[1] == 1:
                                graphlet_cnt[18] += 1
                            if deg[3] == 2 and deg[2] == 2:
                                graphlet_cnt[28] += 1
                        elif e == 8:
                            if deg[3] == 4:
                                graphlet_cnt[22] = graphlet_cnt[22] + 1
                            if deg[3] == 2 and deg[2] == 1:
                                graphlet_cnt[16] = graphlet_cnt[16] + 1
                        elif e == 9:
                            graphlet_cnt[17] = graphlet_cnt[17] + 1
                        elif e == 10:
                            graphlet_cnt[29] = graphlet_cnt[29] + 1

    for v in range(0,g.n):
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
                        e: int = g.countE([v,u,w,x,y])
                        deg: List = list()
                        for _ in range(0,5):
                            deg.append(0)
                        for i in {v,u,w,x,y}:                                
                            deg[g.degree(i, [v,u,w,x,y])] += 1

                        if e == 4:
                            graphlet_cnt[9] += 1
                        elif e == 5:
                            if deg[2] == 5:
                                graphlet_cnt[25] += 1
                            if deg[2] == 1 and deg[3] == 2:
                                graphlet_cnt[26] += 1
                            if deg[2] == 3 and deg[3] == 1 and w in g.nei[y]:
                                graphlet_cnt[11] += 1
                            if deg[2] == 3 and deg[3] == 1 and u in g.nei[y]:
                                graphlet_cnt[12] += 1
                        elif e == 6:
                            if deg[1] == 1 and deg[2] == 1 and deg[3] == 3:
                                graphlet_cnt[14] += 1
                            if deg[2] == 3 and deg[3] == 2 and y not in g.nei[v]:
                                graphlet_cnt[24] += 1
                            if deg[2] == 3 and deg[3] == 2 and y in g.nei[v]:
                                graphlet_cnt[27] += 1
                        elif e == 7:
                            graphlet_cnt[21] += 1

    for v in range(0,g.n):
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

                        e: int = g.countE([v,u,w,x,y])
                        if e == 4:
                            graphlet_cnt[10] += 1

                        

    graphlet_cnt[9] = int(graphlet_cnt[9]/2)
    graphlet_cnt[14] = int(graphlet_cnt[14]/8)
    graphlet_cnt[10] = int(graphlet_cnt[10]/2)
    graphlet_cnt[15] = int(graphlet_cnt[15]/2)
    graphlet_cnt[16] = int(graphlet_cnt[16]/2)
    graphlet_cnt[17] = int(graphlet_cnt[17]/3)
    graphlet_cnt[24] = int(graphlet_cnt[24]/12)
    graphlet_cnt[25] = int(graphlet_cnt[25]/10)
    graphlet_cnt[27] = int(graphlet_cnt[27]/10)
    graphlet_cnt[29] = int(graphlet_cnt[29]/5)

# find exact number of graphlets with 2-5 vertices numbered (0-29)
def exact_graphlet_count(g: Graph) -> None:
    graphlet_cnt : List = list()
    graphlet_cnt.append(g.e)      # G0 : pair of connected vertices
    for _ in range(0,29):
        graphlet_cnt.append(0)

    gc3(g, graphlet_cnt)
    gc4(g, graphlet_cnt)
    gc5(g, graphlet_cnt)

    print("Graphlet Counts:")
    for i in range(0,len(graphlet_cnt)):
        print(f"{i}: {graphlet_cnt[i]}")

if __name__ == "__main__":
    g: Graph = Graph(0,0)
    g.load()

    exact_graphlet_count(g)