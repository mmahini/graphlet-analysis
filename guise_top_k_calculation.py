#!/usr/bin/env python3
import sys, os
sys.path.insert(1, os.getcwd())

from algorithms.exact import Exact
from algorithms.gfd import EpsilonDelta, GfdUtils
from algorithms.guise import Guise
from graph.graphlet import NUM_OF_GRAPHLETS
from graph.graph import Graph, GraphFactory
from concurrent.futures import ThreadPoolExecutor
import time


num_of_running_alg = 10
stationary_steps = 1000
n_steps = 200
m_steps = 1000
k = 5
epsilon = 0.0075

## Test guise graphlet count diff with exact count
def guise_error_calculation():
    n = int(input())
    p = float(input())
    
    guise_correctness_list = list()
    for i in range(num_of_running_alg):
        print(f"run {i} ...")
        guise_correctness = t(n, p)
        if guise_correctness < 0:
            print(f"error!!!, p is smaller than zero")
            continue
        guise_correctness_list.append(guise_correctness)
 
    
    print(f"guise_correctness_average: {sum(guise_correctness_list) / len(guise_correctness_list) * 100}")

def t(n: int, p: float) -> float:
    g: Graph = GraphFactory().get_random_instance(n, p)
    
    exact: Exact = Exact(g)
    exact.run()

    guise_with_n_steps: Guise = Guise(g)
    guise_with_n_steps.run(stationary_steps, n_steps)
    print(f"graphlet_freq={sorted(guise_with_n_steps.gs.graphlet_freq,reverse=True)}")
        
    p = sorted(guise_with_n_steps.gs.graphlet_freq,reverse=True)[k-1] - epsilon
    print(f"p={p}")
    print(f"p correctness:{p <= sorted(exact.gs.graphlet_freq, reverse=True)[k-1]}")
    if p <= 0:
        return -1
        
    m_steps = int(n_steps / (p * 2))
    print(f"m_steps={m_steps}")

    guise_with_m_steps: Guise = Guise(g)
    guise_with_m_steps.run(stationary_steps, m_steps)

    p_prime = sorted(guise_with_m_steps.gs.graphlet_freq,reverse=True)[k - 1] / (1 + epsilon)
    print(f"p_prime={p_prime}")

    t_g_k = list()
    exact_top_graphlet_freq = dict()

    for i in range(NUM_OF_GRAPHLETS):
        exact_top_graphlet_freq[i] = exact.gs.graphlet_freq[i]

        if (guise_with_m_steps.gs.graphlet_freq[i] / (1 - epsilon) > p_prime):
            t_g_k.append(i)

    exact_top_k = [key for key, v in sorted(exact_top_graphlet_freq.items(), reverse=True, key=lambda item: item[1])][0:k]
        
    guise_correctness = len(set(exact_top_k) & set(t_g_k)) / len(exact_top_k)
    
    print(f"t_g_k: {t_g_k}")
    print(f"exact_top_k: {exact_top_k}")
    print(f"guise_correctness: {guise_correctness}")
    print("\n")
    
    return guise_correctness
    
    
if __name__ == "__main__":
    guise_error_calculation()
