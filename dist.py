import numpy as np
import random

c=50
d=c//10
e=c//5
f=e*2
g=6*e//10
h=e//2
l=10

distances=np.full((c,c), np.inf)

for i in range(c):
    for j in range(c):
        distances[i][j]=i//2+j
for i in range(d):
    for j in range(e):
        distances[i][j]=distances[i][j]//10
        distances[i+5][j]=round(distances[i][j]+2,2)
        distances[i][j+d*6]=distances[i][j]*2
        distances[i+h][j+d*8]=round(distances[i][j]//2,2)
for i in range(c):
    for j in range(c):
        if ((i+j)>f):
            distances[i][j]=(i+j)%g
        if (distances[i][j]>f):
            distances[i][j]= distances[i][j]//5+j
        if (distances[i][j]==0):
            distances[i][j]=2
        if (i>j):
            distances[j][i]=distances[i][j]

for j in range(c):
    if (distances[0][j]+distances[j][c-1]<l):
        distances[0][j]=distances[0][j]+l//2
        distances[j][c-1]=distances[j][c-1]+l//3

for i in range(c):
    distances[i][i]=np.inf

for i in range(20*c):
    a= random.randrange(0,c,1)
    b= random.randrange(0,c,1)
    if a==b:
        continue
    else:
        distances[int(a),int(b)], distances[int(b),int(a)] = np.inf, np.inf

# aqi=[]
# for i in range(c):
#     aqi.append(random.randrange(1,10,1))

# for i in range(c):
#     print(f"{i} : {aqi[i]}")
tqi = [1, 4, 8, 8, 6, 7, 7, 2, 2, 8, 9, 6, 1, 4, 5, 5, 4, 8, 6, 6, 1, 9, 5, 9, 9, 1, 8, 9, 9, 7, 7, 2, 6, 1, 9, 3, 7, 8, 5, 3, 2, 8, 2, 1, 9, 8, 1, 2, 5, 4]
print(tqi)

ti = np.full((c,c), 0)

for i in range(c):
    for j in range(c):
        if distances[i][j] == np.inf:
            continue
        else:
            temp = random.randrange(1,5,1)
            ti[i][j], ti[j][i] = temp, temp

# for i in range(c):
#     print(ti[i])

from aco import AntColony
while True:
    source = int(input("Enter source: "))
    dest = int(input("Enter destination: "))
    choice = input("Shaking(Y/N): ")
    if choice=='Y' or choice=='y':
        shaking = True
    else:
        shaking = False

    ant_colony = AntColony(distances, tqi, 500, 1, 10, 0.95, alpha=1, beta=1, gamma=1)
    shortest_path = ant_colony.get_route(start= source, dest= dest, shaking=shaking)
    print("\nOptimal Path :")
    print(shortest_path[0])
    print("\nDistance :")
    print(shortest_path[1])

    print("Choice \n 0: Continue \n 1: Exit \n")
    c = int(input("Enter Choice: "))
    if c==0:
        continue
    elif c==1:
        break
    else:
        print("\nInvalid Choice")
        break

















# distances = np.array([[np.inf,3,4,np.inf,np.inf,np.inf,np.inf,np.inf,np.inf],
#                     [3,np.inf,np.inf,np.inf,np.inf,5,np.inf,np.inf,np.inf],
#                     [4,np.inf,np.inf,5,7,np.inf,np.inf,np.inf,np.inf],
#                     [np.inf,np.inf,5,np.inf,6,np.inf,np.inf,np.inf,np.inf],
#                     [np.inf,np.inf,7,6,np.inf,np.inf,7,np.inf,4],
#                     [np.inf,5,np.inf,np.inf,np.inf,np.inf,1,3,np.inf],
#                     [np.inf,np.inf,np.inf,np.inf,7,1,np.inf,np.inf,4],
#                     [np.inf,np.inf,np.inf,np.inf,np.inf,3,np.inf,np.inf,6],
#                     [np.inf,np.inf,np.inf,np.inf,4,np.inf,4,6,np.inf]])

# distances =  np.array([[np.inf ,14, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,863, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1855,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [14, np.inf ,654, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,916, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,654, np.inf ,985, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,985, np.inf ,1154, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,1154, np.inf ,379, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,379, np.inf ,2553, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,3529, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,2553, np.inf ,41678, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,41678, np.inf ,19602, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,19602, np.inf ,504, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,504, np.inf ,1999, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1999, np.inf ,1884, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1884, np.inf ,4170, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,4170, np.inf ,615, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,615, np.inf ,652, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,652, np.inf ,50930, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,50930, np.inf ,16407, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,16407, np.inf ,122857, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,122857, np.inf ,441, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,441, np.inf ,86, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,86, np.inf ,852, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,852, np.inf ,4014, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,4014, np.inf ,3431, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,3431, np.inf ,42, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,42, np.inf ,607, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,607, np.inf ,489, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,489, np.inf ,97, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,97, np.inf ,169, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,169, np.inf ,12, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,12, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [863, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,367, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,367, np.inf ,6259, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,6259, np.inf ,7454, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,7454, np.inf ,1517, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1517, np.inf ,73, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,73, np.inf ,359, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,359, np.inf ,1570, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1570, np.inf ,272, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,272, np.inf ,622, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,622, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,3529, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1139, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1139, np.inf ,3146, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,3146, np.inf ,1061, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1061, np.inf ,1436, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1436, np.inf ,730, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,730, np.inf ,733, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,733, np.inf ,49, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,49, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,916, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,385, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,385, np.inf ,80, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,80, np.inf ,5935, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,5935, np.inf ,1417, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1417, np.inf ,3467, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,3467, np.inf ,1414, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,1414, np.inf ,231, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,231, np.inf ,84, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,84, np.inf ,32, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,32, np.inf ,152, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,152, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ],
# [1855, np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,9276, np.inf ,np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,9276, np.inf ,723, np.inf ,np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,723, np.inf ,287, np.inf ,np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,287, np.inf ,228, np.inf ],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,228,np.inf ,94],
# [np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,np.inf ,94, np.inf ]])

#print(distances)
# ant_colony = AntColony(distances, 10, 1, 10, 0.95, alpha=1, beta=1)
# shortest_path = ant_colony.get_route(start= 0, dest= 8)
# print("Shortest Path ")
# print(shortest_path[0])
