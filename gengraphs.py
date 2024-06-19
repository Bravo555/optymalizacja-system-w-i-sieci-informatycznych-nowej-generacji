#!/usr/bin/python3

import networkx as nx
from networkx.drawing.nx_pydot import write_dot
import matplotlib.pyplot as plt
import numpy as np


def gen_graph(size):
    g = nx.connected_watts_strogatz_graph(size, 4, 0.5)

    mean = 8
    dev = 2
    for u, v in g.edges():
        weight = np.random.normal(mean, dev)
        g[u][v]['weight'] = int(weight)

    pos = nx.spring_layout(g, seed=7)
    nx.draw(g, pos, with_labels=True, font_weight='bold')
    edge_labels = nx.get_edge_attributes(g, "weight")
    nx.draw_networkx_edge_labels(g, pos, edge_labels)
    plt.savefig(f"K{size}.png")

    pos = nx.nx_agraph.graphviz_layout(g)
    nx.draw(g, pos=pos)
    write_dot(g, f'K{size}.dot')

    plt.clf()

if __name__ == '__main__':
    gen_graph(5)
    gen_graph(10)
    gen_graph(15)
