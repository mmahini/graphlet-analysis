from entities.graphlet import SubGraphlet, SubGraphletFactory, NUM_OF_GRAPHLETS
from entities.graphlet_statistics import GraphletStatistics
from entities.graph import Graph
from random import Random


def random_neighbor(g: Graph, sub_graphlet: SubGraphlet) -> SubGraphlet:
    neighbor_vertices = sub_graphlet.get_neighbor_vertices(g)

    neighbors: list[SubGraphlet] = []

    # sub_graphlet - {i} , sub_graphlet - {i} + {v}
    for i in sub_graphlet.vertices:
        sg: SubGraphlet = SubGraphletFactory().get_copy(sub_graphlet)

        # sub_graphlet - {i}
        sg.remove(i)
        if sg.is_connected():
            neighbors.append(sg)

        # sub_graphlet - {i} + {v}
        for v in neighbor_vertices:
            sg.add(v)
            if sg.is_connected():
                neighbors.append(sg)
            sg.remove(v)

    # sub_graphlet + {v}
    for v in neighbor_vertices:
        sg: SubGraphlet = SubGraphletFactory().get_copy(sub_graphlet)
        sg.add(v)
        neighbors.append(sg)

    # random select from neighbors
    return Random().choice(neighbors)


def get_initial_graphlet(g: Graph) -> SubGraphlet:
    sub_graphlet: SubGraphlet = SubGraphletFactory().get_instance(g)

    v = -1
    for i in g.vertices:
        if len(g.nei[i]) >= 2:
            v = i
            break

    if v == -1:
        print("Shiiiiiiiit !!!")

    sub_graphlet.add(v)

    nei = list(g.nei[v])
    sub_graphlet.add(nei[0])
    sub_graphlet.add(nei[1])

    return sub_graphlet


def calc_stationary_steps(g: Graph) -> int:
    return 100*1000


def get_initial_stationary_point(g: Graph, sub_graphlet: SubGraphlet, stationary_steps: int) -> SubGraphlet:
    for i in range(0, stationary_steps):
        sub_graphlet = random_neighbor(g, sub_graphlet)
    return sub_graphlet


def guise_algorithm(g: Graph, stationary_steps: int, steps: int):
    random_sub_graphlet: SubGraphlet = get_initial_graphlet(g)
    random_sub_graphlet = get_initial_stationary_point(
        g, random_sub_graphlet, stationary_steps)

    gs: GraphletStatistics = GraphletStatistics(g)
    for i in range(0, steps):
        random_sub_graphlet = random_neighbor(g, random_sub_graphlet)
        print(random_sub_graphlet)
        gs.plus_one(random_sub_graphlet.get_graphlet_type())

    gs.calculate_frequencies()
    gs.write_frequencies()
