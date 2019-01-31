import numpy as np
# import pandas as pd
from heapq import *

def heuristic(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2


def astar(array, start, goal):
    # neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

    return 'F'


floor0_stair = np.loadtxt('./All_Data/floor0_stair.csv', delimiter=',')
nmap = np.loadtxt('./All_Data/floor0.csv', delimiter = ',')

# change
floor_stair = floor0_stair
floor = 0

m = floor0_stair.shape[0]
print(m)


# 四个floor 长宽不变
length = nmap.shape[0]  # 11
width = nmap.shape[1]  # 14
a = 0
l_m = 2

S = np.zeros((length, width))

#floor 2
print('**********************************************************************************************************')
print('S_current = \n')
for k in np.arange(1, m + 1):
    stair_pos = (int(float((floor_stair[k-1 , 2]))), int(float((floor_stair[k-1, 3]))))
    for i in range(length):
        for j in range(width):
            if nmap[i, j] != 1:
                step = astar(nmap, stair_pos, (i, j))
                S[i, j] = len(step)
            elif nmap[i, j] == 1:
                S[i, j] = -1  # -1 represents for WALL
            # S_max = max(S_max, S[i, j])
        #     print(int(S[i, j]), '\t', end='')
        # print('i = %d is done\n'%i)
    # print('\n')
    np.savetxt("./All_Data/S_current_%d_%d.csv"%(floor,k), S,  delimiter = ',')
    print('S_current_%d%d OVER \n'%(floor, k))
# S_max = S.max()

print('**********************************************************************************************************')
print('\n')
print('S_{ij} = \n')
for k in np.arange(1, m + 1):
    S = np.loadtxt("./All_Data/S_current_%d_%d.csv"%(floor,k), delimiter = ',')
    S_max = S.max()
    for i in range(length):
        for j in range(width):
            if nmap[i, j] != 1:
                S[i, j] = a * l_m + S_max - S[i, j]
            elif nmap[i, j] == 1:
                S[i, j] = -1  # -1 represents for WALL
    #     print(int(S[i, j]), '\t', end='')
    # print('\n')
    np.savetxt("./All_Data/S_ij_%d_%d.csv"%(floor,k), S,  delimiter = ',')
    print('S_ij_%d%d OVER \n'%(floor,k))




# step = astar(nmap, (0, 0), (1, 1))
# print(step)
# # print(len(step))