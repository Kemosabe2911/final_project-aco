import numpy as np
import random as rn
import sys
import math
from numpy.random import choice as np_choice
from collections import Counter
import datetime

def countDist(myList):
    distList= []
    for i in myList:
        distList.append(i[1])
    pathCount = dict(Counter(distList))
    for key in sorted(pathCount):
        print(f"{key}: {pathCount[key]}")

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
        self.i_pheromone = 1/len(distances)
        #print(np.full((len(distances),len(distances)), 1/len(distances)))
        for i in range(len(distances)):
            self.index_list.append(i)

    def get_route(self, start, dest, shaking):
        td1 = datetime.datetime.now()
        self.start = start
        self.dest = dest
        self.shaking = shaking
        shortest_path = None
        allRoutes = None
        all_time_shortest_path = ("placeholder", np.inf)
        self.initial_pheromone()
        #print(self.pheromone_matrix)
        for i in range(self.n_iterations):
            all_paths = self.get_all_paths(start, dest)
            if not all_paths:
                # print("Paths empty")
                continue
            print(f"\n{i+1} Iteration: ")
            countDist(all_paths)
            self.update_pheromone(all_paths, self.n_best, shortest_path= shortest_path)
            shortest_path = min(all_paths, key=lambda x: x[1])
            longest_path = max(all_paths, key=lambda x: x[1])
            maxDist = longest_path[1]
            # if(i==2):
            #     shaking= ShakingFunction(self.distances, self.pheromone_matrix, maxDist, p=0.2, startEdge= 6, endEdge= 8)
            #     shaking.shaking_pheromones()
            # print(maxDist)
            if(self.shaking and i==2):
                startEdge = int(input("Enter startedge: "))
                endEdge = int(input("Enter endedge: "))
                self.find_shaking_nodes(self.distances, maxDist, p=0.5, startEdge=startEdge, endEdge=endEdge)
                all_time_shortest_path = ("placeholder", np.inf)
                # print(all_time_shortest_path)
                continue
            if self.shaking:
                print(f"\n{i+1} Iteration: ")
                countDist(all_paths)
                print(shortest_path)
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            #print(all_time_shortest_path)
            #self.pheromone *= self.decay
            self.pheromone_decay()
            # allRoutes = all_paths
        td2 = datetime.datetime.now()
        time_diff = td2 - td1
        print(f"\nTime taken: {time_diff.total_seconds()}")
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
            # print(path)
            if(move == dest):
                break
        # print(path)
        return path

    def choose_node(self, pheromone, distance, visited):
        #pheromone = np.copy(pheromone)
        #print(pheromone)
        # print(visited)
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
        # print(row_sum)
        prob = [ p / row_sum for p in prob_list ]
        # print(prob)
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

    def find_shaking_nodes(self, distance, maxDist, p, startEdge, endEdge):
        shaking_nodes_list=[]
        for i in range(len(distance)):
            sub_Colony1 = AntColony(distance,10,1,1,0.95,1,1)
            a= sub_Colony1.get_route(start= startEdge, dest= i,shaking= False)
            b= sub_Colony1.get_route(start= i, dest= endEdge, shaking= False)
            if a[1]< (p*maxDist) or b[1] < (p*maxDist):
                shaking_nodes_list.append(i)
        print("\nShaking Node List:")
        print(shaking_nodes_list)
        self.update_shaking_nodes(shaking_nodes_list, startEdge, endEdge)
        return shaking_nodes_list

    #Shaking Function
    def update_shaking_nodes(self, shaking_nodes, a, b):
        for i in shaking_nodes:
            for j in range(len(self.distances)):
                data = self.pheromone_matrix[i][j]
                if data != 0 :
                    self.pheromone_matrix[i][j] = self.i_pheromone * (1 + math.log(data / self.i_pheromone ))
        self.pheromone_matrix[a][b], self.pheromone_matrix[b][a]= 0,0

# class ShakingFunction(object):
#     #Initialization
#     def __init__(self, distances, pheromone_matrix, maxDist, p, startEdge, endEdge):
#         self.distances = distances
#         self.pheromones = pheromone_matrix
#         self.maxDist = maxDist
#         self.p = p
#         self.startEdge = startEdge
#         self.endEdge = endEdge
#         self.colony = AntColony(distances, 10, 1, 5, 0.95, alpha=1, beta=1)

#     def shaking_pheromones(self):
#         self.find_shaking_nodes(start= self.startEdge, end= self.endEdge)


#     def find_shaking_nodes(self, start, end):
#         shaking_nodes_list=[]
#         for i in range(len(self.distances)):
#             if i==start or i==end:
#                 continue
#             route1= self.colony.get_route(start= start, dest= i)
#             route2= self.colony.get_route(start= i, dest= end)
#             if route1[1]< (self.p * self.maxDist) or route2[1]< (self.p * self.maxDist):
#                 shaking_nodes_list.append(i)
#         print(shaking_nodes_list)
#         return shaking_nodes_list
