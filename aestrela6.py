import heapq

final_config = (1, 2, 3, 4, 12, 13, 14, 5, 11, 0, 15, 6, 10, 9, 8, 7)

sequence = (0, 1, 2, 3, 7, 11, 15, 14, 13, 12, 8, 4, 5, 6, 10, 9)

open_list = []
open_set = set()
closed_list = set()

memo_heuristic = [[0 for x in range(16)] for y in range(16)] 

memo_heuristic[0][0] = 0
memo_heuristic[0][1] = 0
memo_heuristic[0][2] = 0
memo_heuristic[0][3] = 0
memo_heuristic[0][4] = 0
memo_heuristic[0][5] = 0
memo_heuristic[0][6] = 0
memo_heuristic[0][7] = 0
memo_heuristic[0][8] = 0
memo_heuristic[0][9] = 0
memo_heuristic[0][10] = 0
memo_heuristic[0][11] = 0
memo_heuristic[0][12] = 0
memo_heuristic[0][13] = 0
memo_heuristic[0][14] = 0
memo_heuristic[0][15] = 0
memo_heuristic[1][0] = 0
memo_heuristic[1][1] = 1
memo_heuristic[1][2] = 2
memo_heuristic[1][3] = 3
memo_heuristic[1][4] = 1
memo_heuristic[1][5] = 2
memo_heuristic[1][6] = 3
memo_heuristic[1][7] = 4
memo_heuristic[1][8] = 2
memo_heuristic[1][9] = 3
memo_heuristic[1][10] = 4
memo_heuristic[1][11] = 5
memo_heuristic[1][12] = 3
memo_heuristic[1][13] = 4
memo_heuristic[1][14] = 5
memo_heuristic[1][15] = 6
memo_heuristic[2][0] = 1
memo_heuristic[2][1] = 0
memo_heuristic[2][2] = 1
memo_heuristic[2][3] = 2
memo_heuristic[2][4] = 2
memo_heuristic[2][5] = 1
memo_heuristic[2][6] = 2
memo_heuristic[2][7] = 3
memo_heuristic[2][8] = 3
memo_heuristic[2][9] = 2
memo_heuristic[2][10] = 3
memo_heuristic[2][11] = 4
memo_heuristic[2][12] = 4
memo_heuristic[2][13] = 3
memo_heuristic[2][14] = 4
memo_heuristic[2][15] = 5
memo_heuristic[3][0] = 2
memo_heuristic[3][1] = 1
memo_heuristic[3][2] = 0
memo_heuristic[3][3] = 1
memo_heuristic[3][4] = 3
memo_heuristic[3][5] = 2
memo_heuristic[3][6] = 1
memo_heuristic[3][7] = 2
memo_heuristic[3][8] = 4
memo_heuristic[3][9] = 3
memo_heuristic[3][10] = 2
memo_heuristic[3][11] = 3
memo_heuristic[3][12] = 5
memo_heuristic[3][13] = 4
memo_heuristic[3][14] = 3
memo_heuristic[3][15] = 4
memo_heuristic[4][0] = 3
memo_heuristic[4][1] = 2
memo_heuristic[4][2] = 1
memo_heuristic[4][3] = 0
memo_heuristic[4][4] = 4
memo_heuristic[4][5] = 3
memo_heuristic[4][6] = 2
memo_heuristic[4][7] = 1
memo_heuristic[4][8] = 5
memo_heuristic[4][9] = 4
memo_heuristic[4][10] = 3
memo_heuristic[4][11] = 2
memo_heuristic[4][12] = 6
memo_heuristic[4][13] = 5
memo_heuristic[4][14] = 4
memo_heuristic[4][15] = 3
memo_heuristic[5][0] = 4
memo_heuristic[5][1] = 3
memo_heuristic[5][2] = 2
memo_heuristic[5][3] = 1
memo_heuristic[5][4] = 3
memo_heuristic[5][5] = 2
memo_heuristic[5][6] = 1
memo_heuristic[5][7] = 0
memo_heuristic[5][8] = 4
memo_heuristic[5][9] = 3
memo_heuristic[5][10] = 2
memo_heuristic[5][11] = 1
memo_heuristic[5][12] = 5
memo_heuristic[5][13] = 4
memo_heuristic[5][14] = 3
memo_heuristic[5][15] = 2
memo_heuristic[6][0] = 5
memo_heuristic[6][1] = 4
memo_heuristic[6][2] = 3
memo_heuristic[6][3] = 2
memo_heuristic[6][4] = 4
memo_heuristic[6][5] = 3
memo_heuristic[6][6] = 2
memo_heuristic[6][7] = 1
memo_heuristic[6][8] = 3
memo_heuristic[6][9] = 2
memo_heuristic[6][10] = 1
memo_heuristic[6][11] = 0
memo_heuristic[6][12] = 4
memo_heuristic[6][13] = 3
memo_heuristic[6][14] = 2
memo_heuristic[6][15] = 1
memo_heuristic[7][0] = 6
memo_heuristic[7][1] = 5
memo_heuristic[7][2] = 4
memo_heuristic[7][3] = 3
memo_heuristic[7][4] = 5
memo_heuristic[7][5] = 4
memo_heuristic[7][6] = 3
memo_heuristic[7][7] = 2
memo_heuristic[7][8] = 4
memo_heuristic[7][9] = 3
memo_heuristic[7][10] = 2
memo_heuristic[7][11] = 1
memo_heuristic[7][12] = 3
memo_heuristic[7][13] = 2
memo_heuristic[7][14] = 1
memo_heuristic[7][15] = 0
memo_heuristic[8][0] = 5
memo_heuristic[8][1] = 4
memo_heuristic[8][2] = 3
memo_heuristic[8][3] = 4
memo_heuristic[8][4] = 4
memo_heuristic[8][5] = 3
memo_heuristic[8][6] = 2
memo_heuristic[8][7] = 3
memo_heuristic[8][8] = 3
memo_heuristic[8][9] = 2
memo_heuristic[8][10] = 1
memo_heuristic[8][11] = 2
memo_heuristic[8][12] = 2
memo_heuristic[8][13] = 1
memo_heuristic[8][14] = 0
memo_heuristic[8][15] = 1
memo_heuristic[9][0] = 4
memo_heuristic[9][1] = 3
memo_heuristic[9][2] = 4
memo_heuristic[9][3] = 5
memo_heuristic[9][4] = 3
memo_heuristic[9][5] = 2
memo_heuristic[9][6] = 3
memo_heuristic[9][7] = 4
memo_heuristic[9][8] = 2
memo_heuristic[9][9] = 1
memo_heuristic[9][10] = 2
memo_heuristic[9][11] = 3
memo_heuristic[9][12] = 1
memo_heuristic[9][13] = 0
memo_heuristic[9][14] = 1
memo_heuristic[9][15] = 2
memo_heuristic[10][0] = 3
memo_heuristic[10][1] = 4
memo_heuristic[10][2] = 5
memo_heuristic[10][3] = 6
memo_heuristic[10][4] = 2
memo_heuristic[10][5] = 3
memo_heuristic[10][6] = 4
memo_heuristic[10][7] = 5
memo_heuristic[10][8] = 1
memo_heuristic[10][9] = 2
memo_heuristic[10][10] = 3
memo_heuristic[10][11] = 4
memo_heuristic[10][12] = 0
memo_heuristic[10][13] = 1
memo_heuristic[10][14] = 2
memo_heuristic[10][15] = 3
memo_heuristic[11][0] = 2
memo_heuristic[11][1] = 3
memo_heuristic[11][2] = 4
memo_heuristic[11][3] = 5
memo_heuristic[11][4] = 1
memo_heuristic[11][5] = 2
memo_heuristic[11][6] = 3
memo_heuristic[11][7] = 4
memo_heuristic[11][8] = 0
memo_heuristic[11][9] = 1
memo_heuristic[11][10] = 2
memo_heuristic[11][11] = 3
memo_heuristic[11][12] = 1
memo_heuristic[11][13] = 2
memo_heuristic[11][14] = 3
memo_heuristic[11][15] = 4
memo_heuristic[12][0] = 1
memo_heuristic[12][1] = 2
memo_heuristic[12][2] = 3
memo_heuristic[12][3] = 4
memo_heuristic[12][4] = 0
memo_heuristic[12][5] = 1
memo_heuristic[12][6] = 2
memo_heuristic[12][7] = 3
memo_heuristic[12][8] = 1
memo_heuristic[12][9] = 2
memo_heuristic[12][10] = 3
memo_heuristic[12][11] = 4
memo_heuristic[12][12] = 2
memo_heuristic[12][13] = 3
memo_heuristic[12][14] = 4
memo_heuristic[12][15] = 5
memo_heuristic[13][0] = 2
memo_heuristic[13][1] = 1
memo_heuristic[13][2] = 2
memo_heuristic[13][3] = 3
memo_heuristic[13][4] = 1
memo_heuristic[13][5] = 0
memo_heuristic[13][6] = 1
memo_heuristic[13][7] = 2
memo_heuristic[13][8] = 2
memo_heuristic[13][9] = 1
memo_heuristic[13][10] = 2
memo_heuristic[13][11] = 3
memo_heuristic[13][12] = 3
memo_heuristic[13][13] = 2
memo_heuristic[13][14] = 3
memo_heuristic[13][15] = 4
memo_heuristic[14][0] = 3
memo_heuristic[14][1] = 2
memo_heuristic[14][2] = 1
memo_heuristic[14][3] = 2
memo_heuristic[14][4] = 2
memo_heuristic[14][5] = 1
memo_heuristic[14][6] = 0
memo_heuristic[14][7] = 1
memo_heuristic[14][8] = 3
memo_heuristic[14][9] = 2
memo_heuristic[14][10] = 1
memo_heuristic[14][11] = 2
memo_heuristic[14][12] = 4
memo_heuristic[14][13] = 3
memo_heuristic[14][14] = 2
memo_heuristic[14][15] = 3
memo_heuristic[15][0] = 4
memo_heuristic[15][1] = 3
memo_heuristic[15][2] = 2
memo_heuristic[15][3] = 3
memo_heuristic[15][4] = 3
memo_heuristic[15][5] = 2
memo_heuristic[15][6] = 1
memo_heuristic[15][7] = 2
memo_heuristic[15][8] = 2
memo_heuristic[15][9] = 1
memo_heuristic[15][10] = 0
memo_heuristic[15][11] = 1
memo_heuristic[15][12] = 3
memo_heuristic[15][13] = 2
memo_heuristic[15][14] = 1
memo_heuristic[15][15] = 2

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

def HeuristicTwo(read_config):
    wrong_pieces = 0
    for i in range (1,16):
        if read_config[sequence[i - 1]] != 0:
            if (read_config[sequence[i]] != (read_config[sequence[i - 1]] + 1)):
                wrong_pieces += 1
    return wrong_pieces

def HeuristicTree(read_config):
    resp = 0
    for i in range(0,16):
        if (read_config[i] != 0):
            resp = resp + memo_heuristic[read_config[i]][i] 
    return resp

def AStar(initial_config):
    heapq.heappush(open_list, (HeuristicTree(initial_config), 0, initial_config))
    open_set.add(initial_config)
    while(open_list):
        current = heapq.heappop(open_list)
        print('{} : {}' .format(current[1], current[2]))
        open_set.remove(current[2])
        if (current[2] == final_config):
            return(current[1])
        closed_list.add(current[2])
        zero_position = current[2].index(0)
        current_config = list(current[2][:])
        inc_g = current[1] + 1
        for i in swap_position[zero_position]: 
            current_config[zero_position], current_config[i] = current_config[i], current_config[zero_position]
            hx = HeuristicTree(current_config)
            aux = tuple(current_config[:])
            if (aux in closed_list):
                continue
            if (aux not in open_set):
                heapq.heappush(open_list,(hx + inc_g, inc_g, aux))
                open_set.add(aux)
            else:
                index = -1
                achou = False
                while(not achou):
                    index += 1
                    achou = aux == open_list[index][2]
                if(achou) :
                    if ((hx + inc_g) > open_list[index][0]):
                        open_list[index] = open_list[-1]
                        open_list.pop() 
                        heapq.heapify(open_list)
                        heapq.heappush(open_list, (hx + inc_g, inc_g, aux))
            current_config[i], current_config[zero_position] = current_config[zero_position], current_config[i]
                
    print('sem resposta')
    return(-1)
    

read_config = tuple(map(int, input().split()))
print(AStar(read_config))
