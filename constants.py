# -*- coding: utf-8 -*-
from collections import deque

def get_key(dic, value):
    for key in dic:
        if (dic[key] == value):
            return key


def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return  None

def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])
        
# main 8x8 matrix represented as a dictionary  with lists as values
board_matrix = {}

# final key list for rook
store_rook = []

# final key list for knight
store_knight = []

#Stores the current mode
mode = {}

#Graph for Queen
queen_graph = {}

#Graph for Rook
rook_graph = {}

# List to hold final move count in Collector Mode
full_path = []

board_coords = [
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

board_pieces = ['queen', 'knight', 'rook']

valid_coords = ['q',
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']

valid_pieces = ['q', 'test', 'queen', 'knight', 'rook']

valid_modes = ['q', 's', 't', 'c']


Q1 = ['a1', 'b1', 'c1', 'd1', 'a2', 'b2', 'c2', 'd2',
    'a3', 'b3', 'c3', 'd3', 'a4', 'b4', 'c4', 'd4']

Q2 = ['a5', 'b5', 'c5', 'd5', 'a6', 'b6', 'c6', 'd6',
   'a7', 'b7', 'c7', 'd7', 'a8', 'b8', 'c8', 'd8']

Q3 = ['e1', 'f1', 'g1', 'h1', 'e2', 'f2', 'g2', 'h2',
    'e3', 'f3', 'g3', 'h3', 'e4', 'f4', 'g4', 'h4']

Q4 = ['d5', 'e5', 'f5', 'g5', 'h5', 'e6', 'f6', 'g6', 'h6',
     'd7', 'e7', 'f7', 'g7', 'h7', 'e8', 'f8', 'g8', 'h8']


def build_queen_graph():
    for p in board_coords:
        store = []
        pair = board_matrix.get(p)
        x = pair[0]
        y = pair[1]
        #up
        y += 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y -= 1
        #down
        y -= 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y += 1
        #right
        x += 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        x -= 1
        #left
        x -= 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        x += 1
        #di up right
        y += 1
        x += 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y -= 1
        x -= 1
        #di  up left
        y += 1
        x -= 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y -= 1
        x += 1
        #di  down left
        y -= 1
        x -= 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y += 1
        x += 1
        #di  down right
        y -= 1
        x += 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y += 1
        x -= 1
        queen_graph[p] = store
    #pprint.pprint(queen_graph)


def build_rook_graph():
    for p in board_coords:
        store = []
        pair = board_matrix.get(p)
        x = pair[0]
        y = pair[1]
        #up
        y += 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y -= 1
        #down
        y -= 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        y += 1
        #right
        x += 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        x -= 1
        #left
        x -= 1
        k = get_key(board_matrix, [x, y])
        if(k is not None):
            store.append(k)
        rook_graph[p] = store


knight_graph = {

'a1': ['b3', 'c2'],
'b1': ['c3', 'a3', 'd2'],
'c1': ['d3', 'b3', 'a2', 'e2'],
'd1': ['e3', 'c3', 'b2', 'f2'],
'e1': ['f3', 'd3', 'c2', 'g2'],
'f1': ['g3', 'e3', 'd2', 'h2'],
'g1': ['h3', 'f3', 'e2'],
'h1': ['g3', 'f2'],
'a2': ['b4', 'c3', 'c1'],
'b2': ['c4', 'a4', 'd3', 'd1'],
'c2': ['d4', 'b4', 'a3', 'a1', 'e3', 'e1'],
'd2': ['e4', 'c4', 'b3', 'b1', 'f3', 'f1'],
'e2': ['f4', 'd4', 'c3', 'c1', 'g3', 'g1'],
'f2': ['g4', 'e4', 'd3', 'd1', 'h3', 'h1'],
'g2': ['h4', 'f4', 'e3', 'e1'],
'h2': ['g4', 'f3', 'f1'],
'a3': ['b5', 'b1', 'c4', 'c2'],
'b3': ['c5', 'a5', 'c1', 'a1', 'd4', 'd2'],
'c3': ['d5', 'b5', 'd1', 'b1', 'a4', 'a2', 'e4', 'e2'],
'd3': ['e5', 'c5', 'e1', 'c1', 'b4', 'b2', 'f4', 'f2'],
'e3': ['f5', 'd5', 'f1', 'd1', 'c4', 'c2', 'g4', 'g2'],
'f3': ['g5', 'e5', 'g1', 'e1', 'd4', 'd2', 'h4', 'h2'],
'g3': ['h5', 'f5', 'h1', 'f1', 'e4', 'e2'],
'h3': ['g5', 'g1', 'f4', 'f2'],
'a4': ['b6', 'b2', 'c5', 'c3'],
'b4': ['c6', 'a6', 'c2', 'a2', 'd5', 'd3'],
'c4': ['d6', 'b6', 'd2', 'b2', 'a5', 'a3', 'e5', 'e3'],
'd4': ['e6', 'c6', 'e2', 'c2', 'b5', 'b3', 'f5', 'f3'],
'e4': ['f6', 'd6', 'f2', 'd2', 'c5', 'c3', 'g5', 'g3'],
'f4': ['g6', 'e6', 'g2', 'e2', 'd5', 'd3', 'h5', 'h3'],
'g4': ['h6', 'f6', 'h2', 'f2', 'e5', 'e3'],
'h4': ['g6', 'g2', 'f5', 'f3'],
'a5': ['b7', 'b3', 'c6', 'c4'],
'b5': ['c7', 'a7', 'c3', 'a3', 'd6', 'd4'],
'c5': ['d7', 'b7', 'd3', 'b3', 'a6', 'a4', 'e6', 'e4'],
'd5': ['e7', 'c7', 'e3', 'c3', 'b6', 'b4', 'f6', 'f4'],
'e5': ['f7', 'd7', 'f3', 'd3', 'c6', 'c4', 'g6', 'g4'],
'f5': ['g7', 'e7', 'g3', 'e3', 'd6', 'd4', 'h6', 'h4'],
'g5': ['h7', 'f7', 'h3', 'f3', 'e6', 'e4'],
'h5': ['g7', 'g3', 'f6', 'f4'],
'a6': ['b8', 'b4', 'c7', 'c5'],
'b6': ['c8', 'a8', 'c4', 'a4', 'd7', 'd5'],
'c6': ['d8', 'b8', 'd4', 'b4', 'a7', 'a5', 'e7', 'e5'],
'd6': ['e8', 'c8', 'e4', 'c4', 'b7', 'b5', 'f7', 'f5'],
'e6': ['f8', 'd8', 'f4', 'd4', 'c7', 'c5', 'g7', 'g5'],
'f6': ['g8', 'e8', 'g4', 'e4', 'd7', 'd5', 'h7', 'h5'],
'g6': ['h8', 'f8', 'h4', 'f4', 'e7', 'e5'],
'h6': ['g8', 'g4', 'f7', 'f5'],
'a7': ['b5', 'c8', 'c6'],
'b7': ['c5', 'a5', 'd8', 'd6'],
'c7': ['d5', 'b5', 'a8', 'a6', 'e8', 'e6'],
'd7': ['e5', 'c5', 'b8', 'b6', 'f8', 'f6'],
'e7': ['f5', 'd5', 'c8', 'c6', 'g8', 'g6'],
'f7': ['g5', 'e5', 'd8', 'd6', 'h8', 'h6'],
'g7': ['h5', 'f5', 'e8', 'e6'],
'h7': ['g5', 'f8', 'f6'],
'a8': ['b6', 'c7'],
'b8': ['c6', 'a6', 'd7'],
'c8': ['d6', 'b6', 'a7', 'e7'],
'd8': ['e6', 'c6', 'b7', 'f7'],
'e8': ['f6', 'd6', 'c7', 'g7'],
'f8': ['g6', 'e6', 'd7', 'h7'],
'g8': ['h6', 'f6', 'e7'],
'h8': ['g6', 'f7']
    }

