#!/usr/bin/env python3

import os
import ast
from graph.graph import Graph, GraphFactory
from algorithms.guise import Guise
from algorithms.gfd import GfdUtils, EpsilonDelta
from algorithms.exact import Exact
from multiprocessing import Pool, Process

num_of_running_alg = 10
files_path = './t-files'
stationary_steps = 10000
n_steps = 10000


def file_uri_gfd(i=0) -> str:
    return f'{files_path}/gfd_{i}.txt'


def file_uri_gcd(i=0) -> str:
    return f'{files_path}/gcd_{i}.txt'

# initialize error calculation files
# delete existed files from last calculation


def init_files():
    if os.path.isdir(files_path):
        os.system('rm -rf %s' % files_path)
    os.mkdir(files_path)


def calc_guise_error(num_of_run=0, n=0, p=0.0):
    g: Graph = GraphFactory().get_random_instance(n, p)
    # print(g)

    exact: Exact = Exact(g)
    exact.run()

    guise: Guise = Guise(g)
    guise.run(stationary_steps, n_steps)

    gfd_top_kـcorrectness = GfdUtils().calc_gfd_top_kـcorrectness(guise, exact)
    gcd_top_kـcorrectness = GfdUtils().calc_gcd_top_kـcorrectness(guise, exact)

    with open(file_uri_gfd(num_of_run), 'w') as fp:
        fp.write(str(gfd_top_kـcorrectness))

    with open(file_uri_gcd(num_of_run), 'w') as fp:
        fp.write(str(gcd_top_kـcorrectness))


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

    gfd_top_kـcorrectness = list()
    gcd_top_kـcorrectness = list()

    # read calculated errors from file
    for i in range(num_of_running_alg):
        # read gfd errors
        with open(file_uri_gfd(i), 'r') as fp:
            top_kـcorrectness = ast.literal_eval(fp.read())
            gfd_top_kـcorrectness.append(top_kـcorrectness)
        # read vertex gfd errors
        with open(file_uri_gcd(i), 'r') as fp:
            top_kـcorrectness = ast.literal_eval(fp.read())
            gcd_top_kـcorrectness.append(top_kـcorrectness)

    gfd_top_5ـcorrectness = 0
    for i in gfd_top_kـcorrectness:
        gfd_top_5ـcorrectness += i[0]
    print(
        f"\ngfd top 5 correctness: {gfd_top_5ـcorrectness / len(gfd_top_kـcorrectness)}")

    gfd_top_10ـcorrectness = 0
    for i in gfd_top_kـcorrectness:
        gfd_top_10ـcorrectness += i[1]
    print(
        f"\ngfd top 10 correctness: {gfd_top_10ـcorrectness / len(gfd_top_kـcorrectness)}")

    gfd_top_20ـcorrectness = 0
    for i in gfd_top_kـcorrectness:
        gfd_top_20ـcorrectness += i[2]
    print(
        f"\ngfd top 20 correctness: {gfd_top_20ـcorrectness / len(gfd_top_kـcorrectness)}")

    gcd_top_5ـcorrectness = 0
    for i in gcd_top_kـcorrectness:
        gcd_top_5ـcorrectness += i[0]
    print(
        f"\ngcd top 5 correctness: {gcd_top_5ـcorrectness / len(gcd_top_kـcorrectness)}")

    gcd_top_10ـcorrectness = 0
    for i in gcd_top_kـcorrectness:
        gcd_top_10ـcorrectness += i[1]
    print(
        f"\ngcd top 10 correctness: {gcd_top_10ـcorrectness / len(gcd_top_kـcorrectness)}")

    gcd_top_20ـcorrectness = 0
    for i in gcd_top_kـcorrectness:
        gcd_top_20ـcorrectness += i[2]
    print(
        f"\ngcd top 20 correctness: {gcd_top_20ـcorrectness / len(gcd_top_kـcorrectness)}")


if __name__ == '__main__':
    do_calculation()
