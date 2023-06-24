
from graph.graph import Graph, GraphFactory

if __name__ == "__main__":
    n = int(input())
    e = int(input())
    
    g : Graph = GraphFactory().create_instance_with_n_vertices_from(n)            
    
    for _ in range(e):
        i1, i2 = input().split(" ")
        v = int(i1)
        u = int(i2)
        g.nei[v].add(u)
        g.nei[u].add(v)
    
    degrees = 0
    for i in range(n):
        degrees = degrees + len(g.nei[i])
        
    average_degree = degrees / n
    print(f"average degree {average_degree}")