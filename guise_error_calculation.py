#!/usr/bin/env python3

import os
import ast
from graph.graph import Graph, GraphFactory
from algorithms.guise import Guise
from algorithms.gfd import GfdUtils, EpsilonDelta
from algorithms.exact import Exact
from multiprocessing import Pool, Process

num_of_running_alg = 4
files_path = './files'


def file_uri_gfd(i=0) -> str:
    return f'{files_path}/gfd_{i}.txt'


def file_uri_vertex_gfd(i=0) -> str:
    return f'{files_path}/vertex_gfd_{i}.txt'


def file_uri_gdv_vertex_orbits(i=0) -> str:
    return f'{files_path}/gdv_vertex_orbits_{i}.txt'

# initialize error calculation files
# delete existed files from last calculation
def init_files():
    if os.path.isdir(files_path):
        os.system('rm -rf %s/*' % files_path)
    else:
        os.mkdir(files_path)


def calc_guise_error(num_of_run=0, n=0, p=0.0):
    g: Graph = GraphFactory().get_random_instance(n, p)
    # print(g)

    exact: Exact = Exact(g)
    exact.run()

    guise: Guise = Guise(g)
    guise.run(10000, 10000)

    error_gc = GfdUtils().calc_graphlet_count_error(guise, exact)
    error_vgc = GfdUtils().calc_vertex_graphlet_count_error(guise, exact)
    error_voc = GfdUtils().calc_vertex_orbit_count_error(guise, exact)

    with open(file_uri_gfd(num_of_run), 'w') as fp:
        fp.write(str(error_gc))

    with open(file_uri_vertex_gfd(num_of_run), 'w') as fp:
        fp.write(str(error_vgc))

    with open(file_uri_gdv_vertex_orbits(num_of_run), 'w') as fp:
        fp.write(str(error_voc))


def do_calculation():
    num_of_graph_v = int(input())
    num_of_graph_p = float(input())

    print("calculation started, please wait")

    init_files()

    # parallel calculation
    process_list = list()
    for i in range(num_of_running_alg):
        p = Process(
            target=calc_guise_error,
            args=(i, num_of_graph_v, num_of_graph_p))
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()

    graphlet_count_ed = EpsilonDelta([0.1, 0.05, 0.02, 0.01])
    vertex_graphlet_count_ed = EpsilonDelta([0.05, 0.02, 0.01, 0.005])
    vertex_orbit_count_ed = EpsilonDelta([0.01, 0.005, 0.002, 0.001])

    # read calculated errors from file
    for i in range(num_of_running_alg):
        # read gfd errors
        with open(file_uri_gfd(i), 'r') as fp:
            giuse_error = ast.literal_eval(fp.read())
            graphlet_count_ed.append_graphlet_count_error(giuse_error)
        # read vertex gfd errors
        with open(file_uri_vertex_gfd(i), 'r') as fp:
            giuse_error = ast.literal_eval(fp.read())
            vertex_graphlet_count_ed.append_vertex_count_error(giuse_error)
        # read vertex gfd errors
        with open(file_uri_gdv_vertex_orbits(i), 'r') as fp:
            giuse_error = ast.literal_eval(fp.read())
            vertex_orbit_count_ed.append_vertex_count_error(giuse_error)

    graphlet_count_ed.calc_delta()
    vertex_graphlet_count_ed.calc_delta()
    vertex_orbit_count_ed.calc_delta()

    print("\ngraphlet count")
    graphlet_count_ed.write()
    print("\nvertext graphlet count")
    vertex_graphlet_count_ed.write()
    print("\nvertext orbit count")
    vertex_orbit_count_ed.write()


if __name__ == '__main__':
    do_calculation()
