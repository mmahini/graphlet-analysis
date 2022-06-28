# connected components
from typing import List
from graph import Graph

def countE(lst: List) -> int:
    e : int = 0
    for i in lst:
        for j in lst:
            if i in g.nei[j]:
                e = e + 1
    e = e / 2
    return e

def degree(v: int, lst: List) -> int:
    e : int = 0
    for i in lst:
        if i in g.nei[v]:
            e = e + 1
    return e

def gc3(g: Graph, gcnt: List) -> None:
    for v in range(0,g.n):
        for u in g.nei[v]:
            visited: set = {v, u}

            for w in g.nei[v]:
                if w in visited:
                    continue
                visited.add(w)

                if w in g.nei[u]:
                    if w > u and u > v:
                        gcnt[2] = gcnt[2] + 1
                else:
                    if w > u:
                        gcnt[1] = gcnt[1] + 1

def gc4(g: Graph, gcnt: List) -> None:  
    for v in range(0,g.n):
        for u in g.nei[v]:
            for w in g.nei[v]:
                if w <= u:
                    continue
                for x in g.nei[v]:
                    if x <= w:
                        continue
                    if w not in g.nei[u] and w not in g.nei[x] and u not in g.nei[x]:
                        gcnt[4] = gcnt[4] + 1
            
    for v in range(0,g.n):
        for u in g.nei[v]:
            for w in g.nei[u]:
                if w == v:
                    continue
                for x in g.nei[w]:
                    if x == u or x == v:
                        continue
                    e: int = countE([v,u,w,x])
                    if e == 6:
                        gcnt[8] = gcnt[8] + 1
                    elif e == 5:
                        gcnt[7] = gcnt[7] + 1
                    elif e == 3:
                        gcnt[3] = gcnt[3] + 1
                    elif v in g.nei[x]:         # e = 4
                        gcnt[6] = gcnt[6] + 1
                    elif u in g.nei[x]:         # e = 4
                        gcnt[5] = gcnt[5] + 1
    
    gcnt[3] = int(gcnt[3]/2)
    gcnt[5] = int(gcnt[5]/2)
    gcnt[6] = int(gcnt[6]/8)
    gcnt[7] = int(gcnt[7]/12)
    gcnt[8] = int(gcnt[8]/24)


def gc5(g: Graph, gcnt: List) -> None:
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
                        e: int = countE([v,u,w,x,y])
                        deg: List = list()
                        for _ in range(0,5):
                            deg.append(0)
                        for i in {u,w,x,y}:                                
                            deg[degree(i, [v,u,w,x,y])] += 1

                        if e == 4:
                            gcnt[23] = gcnt[23] + 1
                        elif e == 5:
                            gcnt[19] = gcnt[19] + 1
                        elif e == 6:
                            if deg[1] == 1 and deg[2] == 2 and deg[3] == 1:                                
                                gcnt[13] = gcnt[13] + 1
                            if deg[2] == 4: 
                                gcnt[20] = gcnt[20] + 1
                        elif e == 7:
                            if deg[4] == 1 and deg[2] == 3:                                
                                gcnt[15] = gcnt[15] + 1
                            if deg[3] == 3 and deg[1] == 1:
                                gcnt[18] += 1
                            if deg[3] == 2 and deg[2] == 2:
                                gcnt[28] += 1
                        elif e == 8:
                            if deg[3] == 4:
                                gcnt[22] = gcnt[22] + 1
                            if deg[3] == 2 and deg[2] == 1:
                                gcnt[16] = gcnt[16] + 1
                        elif e == 9:
                            gcnt[17] = gcnt[17] + 1
                        elif e == 10:
                            gcnt[29] = gcnt[29] + 1

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
                        e: int = countE([v,u,w,x,y])
                        deg: List = list()
                        for _ in range(0,5):
                            deg.append(0)
                        for i in {v,u,w,x,y}:                                
                            deg[degree(i, [v,u,w,x,y])] += 1

                        if e == 4:
                            gcnt[9] += 1
                        elif e == 5:
                            if deg[2] == 5:
                                gcnt[25] += 1
                            if deg[2] == 1 and deg[3] == 2:
                                gcnt[26] += 1
                            if deg[2] == 3 and deg[3] == 1 and w in g.nei[y]:
                                gcnt[11] += 1
                            if deg[2] == 3 and deg[3] == 1 and u in g.nei[y]:
                                gcnt[12] += 1
                        elif e == 6:
                            if deg[1] == 1 and deg[2] == 1 and deg[3] == 3:
                                gcnt[14] += 1
                            if deg[2] == 3 and deg[3] == 2 and y not in g.nei[v]:
                                gcnt[24] += 1
                            if deg[2] == 3 and deg[3] == 2 and y in g.nei[v]:
                                gcnt[27] += 1
                        elif e == 7:
                            gcnt[21] += 1

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

                        e: int = countE([v,u,w,x,y])
                        if e == 4:
                            gcnt[10] += 1

                        

    gcnt[9] = int(gcnt[9]/2)
    gcnt[14] = int(gcnt[14]/8)
    gcnt[10] = int(gcnt[10]/2)
    gcnt[15] = int(gcnt[15]/2)
    gcnt[16] = int(gcnt[16]/2)
    gcnt[17] = int(gcnt[17]/3)
    gcnt[24] = int(gcnt[24]/12)
    gcnt[25] = int(gcnt[25]/10)
    gcnt[27] = int(gcnt[27]/10)
    gcnt[29] = int(gcnt[29]/5)

#                            print(f"-> {v} {u} {w} {x} {y}")

def gcnt(g: Graph) -> None:
    gcnt : List = list()
    gcnt.append(g.e)      # G0 : pair of connected vertices
    for _ in range(0,29):
        gcnt.append(0)

    gc3(g, gcnt)
    gc4(g, gcnt)
    gc5(g, gcnt)

    print("Graphlet Counts:")
    for i in range(0,len(gcnt)):
        print(f"{i}: {gcnt[i]}")

if __name__ == "__main__":
    g: Graph = Graph(0,0)
    g.load()
    print(g)
    gcnt(g)