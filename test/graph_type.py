#!/usr/bin/env python3

from typing import List
from graph.templates import GraphletTemplates
from graph.graphlet import SubGraphlet, NUM_OF_GRAPHLETS
from utils.graph import GraphUtils

# Test graphlet type calculation based on GraphletTemplates list.
if __name__ == "__main__":
    graphlet_templates = GraphletTemplates().list()
    for i in range(NUM_OF_GRAPHLETS):
        graphlet: SubGraphlet = graphlet_templates[i]
        t = GraphUtils().calc_graphlet_type(graphlet)
        print(f"[{i}] -> {t}")
