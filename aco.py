import numpy as np
import random as rn
from numpy.random import choice as np_choice

class AntColony(object):

    #Initialization
    def __init__(self, distances, n_ants, n_best, n_iterations, p_decay, alpha=1, beta=1):
        self.distances = distances
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        #self.pheromones = np.ones(self.distances.shape) / len(distances)
        self.index_list = []
        self.pheromone_matrix= []
        self.pheromones = np.full(self.distances.shape, 1/len(distances))
        self.decay = p_decay
        self.alpha = alpha
        self.beta = beta
        #print(np.full((len(distances),len(distances)), 1/len(distances)))
        for i in range(len(distances)):
            self.index_list.append(i)

    def get_route(self, start, dest):
        self.start = start
        self.dest = dest
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        self.initial_pheromone()
        #print(self.pheromone_matrix)
        for i in range(self.n_iterations):
            all_paths = self.get_all_paths(start, dest)
            self.update_pheromone(all_paths, self.n_best, shortest_path= shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            #print(shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            #print(all_time_shortest_path)
            #self.pheromone *= self.decay
            self.pheromone_decay()
        return all_time_shortest_path

    def initial_pheromone(self):
        for p_list in self.distances:
            temp_list=[]
            #print(p_list)
            for i in p_list:
                if i == np.inf:
                    temp_list.append(0)
                else:
                    temp_list.append(1/len(self.distances))
            #print(temp_list)
            self.pheromone_matrix.append(temp_list)


    def update_pheromone(self, all_paths, n_best, shortest_path):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        #print(sorted_paths)
        for path, dist in sorted_paths[:n_best]:
            for move in path:
                self.pheromone_matrix[move[0]][move[1]] += 1.0 / self.distances[move]
                self.pheromone_matrix[move[1]][move[0]] = self.pheromone_matrix[move[0]][move[1]]

    def pheromone_decay(self):
        for row in self.pheromone_matrix:
            for data in row:
                data *= self.decay

    def get_all_paths(self, start, dest):
        all_paths=[]
        for i in range(self.n_ants):
            path = self.get_path(start,dest)
            if path == None:
                #print(None)
                continue
            all_paths.append((path, self.get_path_dist(path)))
        return all_paths

    def get_path_dist(self, path):
        total_dist = 0
        for ele in path:
            total_dist += self.distances[ele[0]][ele[1]]
        return total_dist

    def get_path(self, start, dest):
        path=[]
        visited = set()
        visited.add(start)
        prev= start

        #print(self.distances.shape)
        #print("Distances: ")
        #print(self.distances)
        #print(self.pheromones)
        for i in range(len(self.distances)-1):
            next_node = self.choose_node(self.pheromone_matrix[prev], self.distances[prev], visited)
            move = next_node
            if move == None:
                return None
            path.append((prev, move))
            prev = next_node
            visited.add(move)
            #print(path)
            if(move == dest):
                break
        #print(path)
        return path

    def choose_node(self, pheromone, distance, visited):
        #pheromone = np.copy(pheromone)
        #print(pheromone)
        #print(visited)
        for i in list(visited):
            pheromone[i] = 0
        #pheromone[list(visited)] = 0
        if self.check_pheromone_empty(pheromone):
            return None
        prob_list=[]
        for j in range(len(distance)):
            row = (pheromone[j] ** self.alpha) * ((1.0 / distance[j]) ** self.beta)
            prob_list.append(row)
        #row = pheromone ** self.alpha * (( 1.0 / distance) ** self.beta)
        #prob = row / row.sum()
        row_sum= sum(prob_list)
        prob = [ p / row_sum for p in prob_list ]
        #print(prob)
        #print(self.index_list)
        next_node = np_choice(self.index_list, 1, p=prob)[0]
        #print(next_node)
        return next_node

    def check_pheromone_empty(self, pheromone):
        flg=1
        for i in range(len(pheromone)):
            if pheromone[i] != 0:
                flg=0
                break
        if flg==1:
            return True
        else:
            return False
