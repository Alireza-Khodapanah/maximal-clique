import networkx as nx
import matplotlib.pyplot as plt

def create_random_graph(num_nodes, probability):
    graph = nx.erdos_renyi_graph(num_nodes, probability)
    return graph



