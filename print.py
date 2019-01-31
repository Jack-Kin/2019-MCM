import numpy as np
# import pandas as pd
from heapq import *

# def heuristic(a, b):
#     return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
#
#
# def astar(array, start, goal):
#     # neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#     neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#     close_set = set()
#     came_from = {}
#     gscore = {start: 0}
#     fscore = {start: heuristic(start, goal)}
#     oheap = []
#
#     heappush(oheap, (fscore[start], start))
#
#     while oheap:
#
#         current = heappop(oheap)[1]
#
#         if current == goal:
#             data = []
#             while current in came_from:
#                 data.append(current)
#                 current = came_from[current]
#             return data
#
#         close_set.add(current)
#         for i, j in neighbors:
#             neighbor = current[0] + i, current[1] + j
#             tentative_g_score = gscore[current] + heuristic(current, neighbor)
#             if 0 <= neighbor[0] < array.shape[0]:
#                 if 0 <= neighbor[1] < array.shape[1]:
#                     if array[neighbor[0]][neighbor[1]] == 1:
#                         continue
#                 else:
#                     # array bound y walls
#                     continue
#             else:
#                 # array bound x walls
#                 continue
#
#             if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
#                 continue
#
#             if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
#                 came_from[neighbor] = current
#                 gscore[neighbor] = tentative_g_score
#                 fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
#                 heappush(oheap, (fscore[neighbor], neighbor))
#
#     return 'F'
#
# floor2_stair = np.load('./floor_data/floor2_stair.npy')
# # nmap_m1 = np.loadtxt('./floor_data/floorm1.csv', delimiter = ',')
# # nmap_0 = np.loadtxt('./floor_data/floor0.csv', delimiter = ',')
# # nmap_1 = np.loadtxt('./floor_data/floorm1.csv', delimiter = ',')
# nmap_2 = np.loadtxt('./floor_data/floor2.csv', delimiter = ',')
#
# print(floor2_stair)
# print((float(floor2_stair[1, 2]), float(floor2_stair[1, 3])))
# # 四个floor 长宽不变
# length = nmap_2.shape[0]  # 11
# width = nmap_2.shape[1]  # 14
# a = 0
# l_m = 2


floorm1_stair = np.loadtxt('./All_Data/floorm1_stair.csv', delimiter=',')
floorm1_door = np.loadtxt('./All_Data/floorm1_door.csv', delimiter=',')
floor0_stair = np.loadtxt('./All_Data/floor0_stair.csv', delimiter=',')
floor0_door = np.loadtxt('./All_Data/floor0_door.csv', delimiter=',')
floor1_stair = np.loadtxt('./All_Data/floor1_stair.csv', delimiter=',')
floor2_stair = np.loadtxt('./All_Data/floor2_stair.csv', delimiter=',')


print('floorm1_stair')
print(floorm1_stair)
print('\n')
print('floorm1_door')
print(floorm1_door)
print('\n')
print('floor0_stair')
print(floor0_stair)
print('\n')
print('floor0_door')
print(floor0_door)
print('\n')
print('floor1_stair')
print(floor1_stair)
print('\n')
print('floor2_stair')
print(floor2_stair)
print('\n')
# arr = np.array([5,2,10,1])
# print(arr)
# print(arr[0])
# maxindex  = np.argmax(arr)
# print(maxindex)
# door1_data = [(67,10),(68,10),(69,10),(70,10)]
# print(door1_data[0])
# x = door1_data[0]

# print(floor1_stair.shape[0])

# #floor1中多个楼梯
# for i in range(int(floor1_stair.shape[0])):
#     stair_pos = []
#     for j in range(int(floor1_stair[i][10]), int(floor1_stair[i][12] + 1)):
#         for k in range(int(floor1_stair[i][11]), int(floor1_stair[i][13] + 1)):
#             stair_pos = stair_pos + [(j, k)]
#             # print(( j, k))
#
#     print(stair_pos)
#
# floor = 1
# num = 2
# m = 3
# print("S_current_%d%d_%d.csv"%(floor,num,m))
