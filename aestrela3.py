import heapq
import copy
import string

final_config = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]
open_list = []
closed_list = set()

swap_position = [[1,4],
                 [0,2,5],
                 [1,3,6],
                 [2,7],
                 [0,5,8],
                 [1,6,9,4],
                 [2,7,10,5],
                 [3,6,11],
                 [4,9,12],
                 [5,10,13,8],
                 [6,11,14,9],
                 [7,15,10],
                 [8,13],
                 [9,14,12],
                 [10,15,13],
                 [11,14]]

def HeuristicTree(read_config):

    manhattanDistanceSum = 0
    for i in range(0,16):
        value = read_config[i]
        if(value != 0):
            targetX = int((value)/4)
            targetY = int((value)%4)
            target_position = final_config.index(value)
            tx = int((target_position)/4)
            ty = int((target_position)%4)
            manhattanDistanceSum = manhattanDistanceSum + abs(targetX - tx)+ abs(targetY - ty)
    return manhattanDistanceSum

def GetChildren(current_config, g_function):
    zero_position = current_config.index(0)
    inc_g = g_function + 1
    for i in swap_position[zero_position]:
            current_config[zero_position], current_config[i] = current_config[i], current_config[zero_position]
            aux_current = current_config[:]
            if (str(aux_current)) not in closed_list:
                heapq.heappush(open_list, (HeuristicTree(aux_current) + inc_g, inc_g, aux_current))
            current_config[zero_position], current_config[i] = current_config[i], current_config[zero_position]

def AStar(initial_config):
    heapq.heappush(open_list,(HeuristicTree(initial_config), 0, initial_config) )
    current_state = heapq.heappop(open_list)
    while(HeuristicTree(current_state[2])):
        closed_list.update([str(current_state[2])])
        GetChildren(current_state[2], current_state[1])
        current_state = heapq.heappop(open_list)
    print(current_state[1])

read_config = list(map(int, input().split()))
AStar(read_config)
