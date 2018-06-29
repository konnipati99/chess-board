# -*- coding: utf-8 -*-
import argparse
from constants import *
import random


def queen_target_mode(data, target, opposition , path):
    intial_location = data[1]
    goal = target[1]
    print "Shortest path from {} to {}".format(intial_location, goal)
    print "{}".format(path)
    for i in range(0, len(path)):
        if(path[i] in opposition):
            print "Black Queen captures White Pawn at {}!\n".format(path[i])
            break
    print "\n"


def rook_target_mode(data, target, opposition, path):
    intial_location = data[1]
    goal = target[1]
    print "Shortest path from {} to {}".format(intial_location, goal)
    print "{}".format(path)
    for i in range(0, len(path)):
        if(path[i] in opposition):
            print "Black Rook captures White Pawn at {}!\n".format(path[i])
            break
    print "\n"


def knight_target_mode(data, target, opposition, path):
    intial_location = data[1]
    goal = target[1]
    print "Shortest path from {} to {}".format(intial_location, goal)
    print "{}".format(path)
    for i in range(0, len(path)):
        if(path[i] in opposition):
            print "Black Knight captures White Pawn at {}!\n".format(path[i])
            break
    print "\n"


def target_mode_service_init():
    build_queen_graph()
    build_rook_graph()


def find_furthest(coord):
    if(coord in Q1):
        return ['Q1', 'h8']
    if(coord in Q2):
        return ['Q2', 'h1']
    if(coord in Q3):
        return ['Q3', 'a8']
    if(coord in Q4):
        return ['Q4', 'a1']



def get_random_pieces(start_coord):
    #Copy list
    new_list = board_coords[:]

    # Remove element
    new_list.remove(start_coord)

    #create randomized list
    random.shuffle(new_list)

    # Take the first 8 elements of the now randomized list
    return new_list[0:8]


def target_mode_service_run(data):
    target = find_furthest(data[1])
    print "Initial Postion: {}    ".format(data[1]),
    print "Target Position: {} ".format(target[1])
    opposition = get_random_pieces(data[1])
    print opposition
    if(data[0] == 'queen'):
        s_path = shortest_path(queen_graph, data[1], target[1])
        queen_target_mode(data, target, opposition , s_path)
    if(data[0] == 'rook'):
        s_path = shortest_path(rook_graph, data[1], target[1])
        rook_target_mode(data, target, opposition , s_path)
    if(data[0] == 'knight'):
        s_path = shortest_path(knight_graph, data[1], target[1])
        knight_target_mode(data, target, opposition , s_path)

def rules_service_init():
    i = 0
    #fill board_matrix with string represintations of coords
    for x in range(0, 8):
        for y in range(0, 8):
            # set each coord(a1,b5, etc) to a location in board_matrix.
            board_matrix[board_coords[i]] = [y, x]
            i += 1


if __name__ == '__main__':
    rules_service_init()
    target_mode_service_init()

    parser = argparse.ArgumentParser()
    # Add arguments
    parser.add_argument(
        '-target', '--target', type=str, help='target', required=True)

    parser.add_argument(
        '-position', '--position', type=str, help='Position', required=True)
    
    args = vars(parser.parse_args())

    #List to hold the Chess piece and starting coordinate
    data_pair = []
    data_pair.append(args['target'])
    data_pair.append(args['position'])
    data_pair.append('T')

    if not args:

        print "Usage: python code_exercise2.py -target knight -position d2"

    else:
        target_mode_service_run(data_pair)
    
