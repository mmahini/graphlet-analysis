#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

from typing import List
from graph.graph import Graph, GraphFactory
from graph.algorithms.gfd import GfdUtils

from algorithms.epsilon_delta import EpsilonDelta
from graph.graph import Graph, GraphFactory
from graph.algorithms.guise import Guise
from graph.algorithms.gfd import GfdUtils
from graph.algorithms.exact import Exact
from multiprocessing import Pool, Process



# Generate a random graph base on Erdos-Renyi.
if __name__ == "__main__":
    n = int(input())
    p = float(input())

    g: Graph = GraphFactory().get_random_instance(n, p)
    g.write()
