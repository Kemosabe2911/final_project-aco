from dist import distances
import numpy as np
from aco import AntColony

ant_colony = AntColony(distances, 100, 1, 10, 0.95, alpha=1, beta=1)
shortest_path = ant_colony.get_route(start= 0, dest= 10, shaking=False)
print("\nShortest Path :")
print(shortest_path[0])
print("\nDistance :")
print(shortest_path[1])

