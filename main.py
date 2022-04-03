from dist import distances
import numpy as np
from aco import AntColony


ant_colony = AntColony(distances, 10, 1, 5, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.get_route(start= 0, dest= 8)
print("Shortest Path :")
print(shortest_path[0])
print("Distance :")
print(shortest_path[1])