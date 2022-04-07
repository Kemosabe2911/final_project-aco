from dist import distances
import numpy as np
from aco import AntColony
import networkx as nx
import string

# G = nx.from_numpy_matrix(distances)
# G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

# G = nx.to_agraph(G)

# G.node_attr.update(color="red", style="filled")
# G.edge_attr.update(color="blue", width="2.0")

# G.draw('distances.png', format='png', prog='neato')

ant_colony = AntColony(distances, 50, 1, 10, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.get_route(start= 0, dest= 8)
print("\nShortest Path :")
print(shortest_path[0])
print("\nDistance :")
print(shortest_path[1])