from graph.graph import Graph, GraphFactory

if __name__ == "__main__":
    g: Graph = GraphFactory().load_graph_from_cmd()

    n = g.countV()
    degrees = 0
    for i in range(n):
        degrees = degrees + len(g.nei[i])

    average_degree = degrees / n
    print(f"average degree {average_degree}")
