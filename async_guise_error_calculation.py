import os

from concurrent.futures import ThreadPoolExecutor
from entities.graph import Graph, GraphFactory
from guise.guise import Guise
from graph_algorithms.gfd_algorithm import GfdUtils, EpsilonDelta
from exact.exact_graphlet_count import Exact
from multiprocessing import Pool, Process

num_of_running_alg = 20
files_path = './files'


def file_uri(i=0) -> str:
    return f'{files_path}/{i}.txt'


def init_files():
    if os.path.isdir(files_path):
        os.system('rm -rf %s/*' % files_path)
    else:
        os.mkdir(files_path)


def calc_guise_error(num_of_run=0, n=0, p=0.0):
    print(f'run {num_of_run} ...')

    g: Graph = GraphFactory().get_random_instance(n, p)
    # print(g)

    exact: Exact = Exact(g)
    exact.run()

    guise: Guise = Guise(g)
    guise.run(10000, 10000)

    guise_error = GfdUtils().calc_giuse_error(guise, exact)

    with open(file_uri(num_of_run), 'w') as fp:
        fp.write(str(guise_error))


def do_calculation():
    num_of_graph_v = int(input())
    num_of_graph_p = float(input())

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

    epsilonDelta = EpsilonDelta()
    # read calculated errors from file
    for i in range(num_of_running_alg):
        with open(file_uri(i), 'r') as fp:
            giuse_error = fp.read()[1:-1]
            giuse_error = [float(i) for i in giuse_error.split((', '))]
            epsilonDelta.append_error(giuse_error)

    epsilonDelta.calc_delta()
    epsilonDelta.write()


if __name__ == '__main__':
    do_calculation()
