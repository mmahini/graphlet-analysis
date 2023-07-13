
from graph.graph import Graph, GraphFactory

if __name__ == "__main__":
    n = int(input())
    e = int(input())
    
    g : Graph = GraphFactory().create_instance_with_n_vertices_from(n)            
    
    for _ in range(e):
        i1, i2, i3= input().split(" ")
        v = int(i1)
        u = int(i2)
        g.nei[v].add(u)
        g.nei[u].add(v)
        
    g.write()