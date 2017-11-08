import heapq
import copy

final_config = [1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7]

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

def HeuristicOne(read_config):
    wrong_pieces = 0
    for i in range(0,16):
        if read_config[i] != 0:
            if (read_config[i] != final_config[i]):
                wrong_pieces += 1
    return wrong_pieces

def GetChildren(current_config, open_list, g_function):
    zero_position = current_config.index(0)
    for i in swap_position[zero_position]:
        current_config[zero_position], current_config[i] = current_config[i], current_config[zero_position]
        new_current = copy.copy(current_config)
        h_function = HeuristicOne(current_config)
        heapq.heappush(open_list, (h_function + g_function + 1, g_function + 1, new_current))
        current_config[zero_position], current_config[i] = current_config[i], current_config[zero_position]

def AStar(initial_config):
    open_list = []
    heapq.heappush(open_list, (HeuristicOne(initial_config), 0, initial_config))
    current_state = heapq.heappop(open_list)
    while(HeuristicOne(current_state[2])):
        GetChildren(current_state[2], open_list, current_state[1])
        current_state = heapq.heappop(open_list)
    print(current_state[1])
    

read_config = list(map(int, input().split()))
'''print(HeuristicOne(read_config))'''
AStar(read_config)