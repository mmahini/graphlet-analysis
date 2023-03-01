#!/usr/bin/env python3

from typing import List
from graph.templates import GraphletTemplates
from utils.graph import GraphUtils

# Print predefined graphlet templates based on The Paper
if __name__ == "__main__":
    graphlet_templates = GraphletTemplates().list()
    for (k, graphlet) in graphlet_templates.items():
        print(f"[{k}] -> {GraphUtils().degree_map(graphlet)}")

    count = 0
    for (k1, g1) in graphlet_templates.items():
        for (k2, g2) in graphlet_templates.items():
            if GraphUtils().is_isomorph(g1, g2):
                count += 1
    print(f"{count} should be 30.")
