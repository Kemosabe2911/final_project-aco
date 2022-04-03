import numpy as np
from aco import AntColony

distances = np.array([[np.inf,3,4,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf],
                    [3,np.inf,np.inf,np.inf,np.inf,5,np.inf,np.inf,np.inf],
                    [4,np.inf,np.inf,5,7,np.inf,np.inf,np.inf,np.inf],
                    [np.inf,np.inf,5,np.inf,6,np.inf,np.inf,np.inf,np.inf],
                    [np.inf,np.inf,7,6,np.inf,np.inf,7,np.inf,4],
                    [np.inf,5,np.inf,np.inf,np.inf,np.inf,1,3,np.inf],
                    [np.inf,np.inf,np.inf,np.inf,7,1,np.inf,np.inf,4],
                    [np.inf,np.inf,np.inf,np.inf,np.inf,3,np.inf,np.inf,6],
                    [np.inf,np.inf,np.inf,np.inf,4,np.inf,4,6,np.inf]])

#print(distances)
# ant_colony = AntColony(distances, 10, 1, 10, 0.95, alpha=1, beta=1)
# shortest_path = ant_colony.get_route(start= 0, dest= 8)
# print("Shortest Path ")
# print(shortest_path[0])
